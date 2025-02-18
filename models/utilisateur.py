from database.db import db
from tinydb import Query

class Utilisateur:
    def __init__(self, nom: str, email: str, mot_de_passe: str, role:  str)->None:
        self._nom = nom
        self._email = email
        self._mot_de_passe = mot_de_passe
        self._role = role

    # Getters
    @property
    def nom(self) -> str:
        return self._nom
    @nom.setter
    def nom(self, nom: str) -> None:
        self._nom = nom

    @property
    def email(self) -> str:
        return self._email
    @email.setter
    def email(self, email: str) -> None:
        self._email = email
    @property
    def mot_de_passe(self) -> str:
        return self._mot_de_passe
    @mot_de_passe.setter
    def mot_de_passe(self, mot_de_passe: str) -> None:
        self._mot_de_passe = mot_de_passe

    @property
    def role(self) -> str:
        return self._role
    @role.setter
    def role(self, role: str) -> None:
        self._role = role

    def sauvegarder(self):
        """Enregistrer les donnees dans la base"""
        utilisateur_table = db.table("utilisateur")
        utilisateur_table.insert({
            "nom": self._nom,
            "email": self._email,
            "mot_de_passe": self._mot_de_passe,
            "role": self._role
        })
    @staticmethod
    def trouver_par_email(email: str) -> "Utilisateur":
        utilisateur_table = db.table("utilisateur")
        User = Query()
        utilisateur = utilisateur_table.get(User.email==email)
        return utilisateur

