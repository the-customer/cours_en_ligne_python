from models.utilisateur import Utilisateur


class Admin(Utilisateur):
    def __init__(self, nom: str, email: str, mot_de_passe: str)->None:
        super().__init__(nom, email, mot_de_passe, "admin")