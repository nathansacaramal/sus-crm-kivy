# O modelo de dados (entidade) independe do Kivy.
# Classes normais do Python representam a informação que a interface gráfica (app) vai manipular.
from dataclasses import dataclass


@dataclass(frozen=True)
class Patient:
    name: str
    cpf: str
    sus_card: str
    phone: str
    city: str