from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from app.ui.page_container import PageContainer


# Herdando de `Screen`, essa classe se torna uma tela que pode ser gerenciada
# pelo ScreenManager da nossa aplicação.
class PatientFormScreen(Screen):
    def __init__(self, patient_service, **kwargs):
        super().__init__(**kwargs)

        self.patient_service = patient_service

        # layout será o contêiner onde vamos colocar todos os nossos campos.
        # No Kivy, usamos layouts (como BoxLayout) para organizar os widgets na tela.
        layout = PageContainer()

        # Label é um componente de texto estático.
        title = Label(
            text="[b]CRM SUS - Cadastro de Pacientes[/b]",
            markup=True,  # markup=True permite usar tags (como [b] de bold/negrito) no texto
            font_size=22,
            # size_hint_y controla a altura do elemento (1.0 = 100%, 0.12 = 12%)
            # em proporção ao espaço disponível no layout pai.
            size_hint_y=0.12,
        )

        # TextInput é o campo interativo onde o usuário digita informações.
        self.name_input = TextInput(
            hint_text="Nome completo", # hint_text é o texto de "placeholder" que some ao digitar
            multiline=False, # multiline=False obriga a ser um campo de linha única
            size_hint_y=0.1,
        )

        self.cpf_input = TextInput(
            hint_text="CPF",
            multiline=False,
            size_hint_y=0.1,
        )

        self.sus_card_input = TextInput(
            hint_text="Cartão SUS",
            multiline=False,
            size_hint_y=0.1,
        )

        self.phone_input = TextInput(
            hint_text="Telefone",
            multiline=False,
            size_hint_y=0.1,
        )

        self.city_input = TextInput(
            hint_text="Cidade",
            multiline=False,
            size_hint_y=0.1,
        )

        # Button é um botão clicável.
        save_button = Button(
            text="Cadastrar paciente",
            size_hint_y=0.12,
        )

        # O método `bind` serve para escutar eventos. O evento 'on_press' dispara ao clicar no botão.
        # Quando clicarem, a função `self.save_patient` será chamada.
        save_button.bind(on_press=lambda *_: self.save_patient())

        self.feedback_label = Label(
            text="Preencha os dados do paciente.",
            size_hint_y=0.12,
        )

        self.patient_list_label = Label(
            text="Pacientes cadastrados aparecerão aqui.",
            size_hint_y=0.34,
        )

        # add_widget anexa (coloca) os componentes dentro do nosso layout.
        # A ordem em que são adicionados importa: neste caso, serão desenhados de cima para baixo.
        layout.add_widget(title)
        layout.add_widget(self.name_input)
        layout.add_widget(self.cpf_input)
        layout.add_widget(self.sus_card_input)
        layout.add_widget(self.phone_input)
        layout.add_widget(self.city_input)
        layout.add_widget(save_button)
        layout.add_widget(self.feedback_label)
        layout.add_widget(self.patient_list_label)

        self.add_widget(layout)

    def save_patient(self) -> None:
        name = self.name_input.text.strip() # .strip() é um método de strings usado para remover espaços em branco (ou outros caracteres) do início e do fim de um texto.
        cpf = self.cpf_input.text.strip()
        sus_card = self.sus_card_input.text.strip()
        phone = self.phone_input.text.strip()
        city = self.city_input.text.strip()

        if not name or not cpf or not sus_card:
            self.feedback_label.text = "Nome, CPF e Cartão SUS são obrigatórios."
            return

        patient = self.patient_service.create_patient(
            name=name, # nome que será armazenado
            cpf=cpf,
            sus_card=sus_card,
            phone=phone,
            city=city,
        )

        self.feedback_label.text = (
            f"Paciente {patient.name} cadastrado com sucesso."
        )

        self.clear_form()
        self.refresh_patient_list()

    def clear_form(self) -> None:
        self.name_input.text = ""   #limpa o campo
        self.cpf_input.text = ""
        self.sus_card_input.text = ""
        self.phone_input.text = ""
        self.city_input.text = ""

    def refresh_patient_list(self) -> None:
        patients = self.patient_service.list_patients()

        if not patients:
            self.patient_list_label.text = (
                "Nenhum paciente cadastrado."
            )
            return

        lines = []

        for index, patient in enumerate(patients, start=1): #aqui você percorre a lista de pacientes e concatena com |, quebrando a linha com \n. \n = <br> no html
            lines.append(
                f"{index}. {patient.name} | "
                f"SUS: {patient.sus_card} | " 
                f"Cidade: {patient.city}"
            )

        self.patient_list_label.text = "\n".join(lines)