from database.db import db
class Cours:
    def __init__(self, titre: str, description: str, prix: int, prof_email: str)->None:
        self.titre = titre
        self.description = description
        self.prix = prix
        self.prof_email = prof_email
        self.etudiants_inscrits = []

    def sauvegarder(self):
        cours_table = db.table('cours')
        cours_table.insert({
            'titre': self.titre,
            'description': self.description,
            'prix': self.prix,
            'prof_email': self.prof_email,
            'etudiants_inscrits': self.etudiants_inscrits
        })