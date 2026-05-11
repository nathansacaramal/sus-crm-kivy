from kivy.uix.boxlayout import BoxLayout


# BoxLayout é um dos layouts mais essenciais do Kivy. Ele empilha widgets em uma linha ou coluna.
class PageContainer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical", # "vertical" empilha de cima para baixo. "horizontal" (da esq pra dir) é o padrão.
            padding=20,# padding: espaço interno (margem interna) entre a borda do layout e os itens.
            spacing=10,# spacing: espaço entre cada um dos itens (widgets filhos) dentro do layout.
            **kwargs,
        )