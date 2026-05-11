from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from app.screens.patient_form_screen import (
    PatientFormScreen,
)
from app.services.patient_service import (
    PatientService,
)


# Toda aplicação Kivy deve ter uma classe principal que herda de `App`.
class SusCrmApp(App):
    # O método `build` é o coração da sua aplicação. Ele é chamado quando
    # o app inicia e DEVE retornar o widget raiz (o componente principal da tela).
    def build(self):
        # Define o título da janela do aplicativo
        self.title = (
            "CRM SUS - Cadastro de Pacientes"
        )

        patient_service = PatientService()

        # ScreenManager é um gerenciador que permite navegar entre múltiplas
        # telas (Screens). Aqui, ele é o nosso widget raiz.
        screen_manager = ScreenManager()

        # Adicionamos nossa tela de formulário ao gerenciador.
        screen_manager.add_widget(
            PatientFormScreen(
                patient_service=patient_service,
                name="patient_form",  # Toda Screen precisa de um 'name' para o ScreenManager identificá-la
            )
        )

        return screen_manager


if __name__ == "__main__":
    SusCrmApp().run()