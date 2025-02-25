from tinydb import Query
from database.db import db

class CoursController:
    @staticmethod
    def afficher_cours_diponibles():
        cours_table = db.table("cours")
        cours = cours_table.all()
        if not cours :
            print("❌ Aucun cours disponible")
            return None
        print("=========> 📚 Cours disponibles 📚 <=========\n")
        for i,c in enumerate(cours,start=1):
            print(f"{i}. {c['titre']} - {c['prix']}cfa")
        return cours


    @staticmethod
    def inscrire_etudiant(email_etudiant):
        cours = CoursController.afficher_cours_diponibles()
        if cours is None:
            return 
        choix = int(input("Choisissez un cours à suivre (numéro) : ")) - 1
        if choix < 0 or choix >= len(cours):
            print("❌ Choix invalide")
            return
        cours_choisi = cours[choix]
        cours_table = db.table("cours")
        etudiant_table = db.table("utilisateur")
        User = Query()

        etudiant = etudiant_table.get(User.email == email_etudiant)
        if etudiant is None:
            print("❌ Etudiant non trouvé")
            return
        if etudiant['solde'] < cours_choisi['prix']:
            print("❌ Solde insuffisant. Veuillez recharger votre compte 💵")
            return
        nouveau_solde = etudiant['solde'] - cours_choisi['prix']
        etudiant_table.update({'solde': nouveau_solde}, User.email == email_etudiant)
        #
        cours_choisi["etudiants_inscrits"].append(email_etudiant)
        cours_table.update({'etudiants_inscrits': cours_choisi['etudiants_inscrits']}, Query().titre == cours_choisi['titre'])
        print(f"✅ Inscription réussie au cours '{cours_choisi['titre']}'. Nouveau solde : {nouveau_solde} fcfa")
        