from models.utilisateur import Utilisateur

class Etudiant(Utilisateur):
    def __init__(self, nom: str, email: str, mot_de_passe: str)->None:
        super().__init__(nom, email, mot_de_passe, "etudiant")
        self._solde = 0

    # Getters
    @property
    def solde(self) -> int:
        return self._solde
    @solde.setter
    def solde(self, solde: int) -> None:
        self._solde = solde
    
    def recharger_solde(self, montant: int) -> None:
        self._solde += montant