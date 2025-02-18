from models.utilisateur import Utilisateur
from models.etudiant import Etudiant
from models.professeur import Professeur
from models.admin import Admin


class UtilisateurController:
    @staticmethod
    def creer_utilisateur():
        nom = input("Entrez le nom : ")
        email = input("Entrez l'email : ")
        mot_de_passe = input("Entrez le mot de passe : ")
        role = input("Entrez le role [etudiant, professeur, admin] : ")

        if role == "etudiant":
            utilisateur = Etudiant(nom, email, mot_de_passe)
        elif role == "professeur":
            utilisateur = Professeur(nom, email, mot_de_passe)
        elif role == "admin":
            utilisateur = Admin(nom, email, mot_de_passe)
        else:
            print("Role invalide")
            return
        utilisateur.sauvegarder()
        print(f"<{utilisateur.role.capitalize()}> {utilisateur.nom} a été créé avec succès")

    @staticmethod
    def connexion():
        email = input("Entrez l'email : ")
        mot_de_passe = input("Entrez le mot de passe : ")

        utilisateur = Utilisateur.trouver_par_email(email)

        if utilisateur and utilisateur['mot_de_passe'] == mot_de_passe:
            print(f"Bienvenue {utilisateur['nom']} !")
            return utilisateur
        else:
            print("Email ou mot de passe invalide")
            return None