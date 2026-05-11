from app.domain.patient import Patient


# Camada de serviço: encapsula as regras de negócio e o estado da aplicação
# (neste caso, a lista de pacientes em memória).
class PatientService:
    def __init__(self) -> None:
        self._patients: list[Patient] = []

    def create_patient(
        self,
        name: str,
        cpf: str,
        sus_card: str,
        phone: str,
        city: str,
    ) -> Patient:
        patient = Patient(
            name=name,
            cpf=cpf,
            sus_card=sus_card,
            phone=phone,
            city=city,
        )

        self._patients.append(patient)

        return patient

    def list_patients(self) -> list[Patient]:
        return self._patients.copy()