from tinydb import Query
from database.db import db
from models.utilisateur import Utilisateur

class Paiement:

    def __init__(self, email_etudiant: str, montant: int)->None:
        self.email_etudiant = email_etudiant
        self.montant = montant

    def enregistrer_paiement_credit(self):
        paiement_table = db.table('paiements')
        paiement_table.insert({
            'email_etudiant': self.email_etudiant, 
            'montant': self.montant
        })
        #
        etudiant = Utilisateur.trouver_par_email(self.email_etudiant)
        if not etudiant:
            print("❌ L'étudiant n'existe pas")
            return
        nouveau_solde = etudiant['solde'] + self.montant
        table_etudiants = db.table('utilisateur')
        User = Query()
        table_etudiants.update({'solde': nouveau_solde}, User.email == self.email_etudiant)
        print(f"✅ Dépôt reussi avec succès! Nouveau solde : {nouveau_solde}")