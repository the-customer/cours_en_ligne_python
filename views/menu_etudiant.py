from controllers.paiement_controller import PaiementController
from controllers.cours_controller import CoursController
from controllers.certification_controller import CertificationController as certifCtrl
from controllers.evaluation_controller import EvaluationController as evalCtrl


class MenuEtudiant:
    @staticmethod
    def afficher_menu(email):
        while True:
            print("++++++ 🙇‍♀️ Menu Etudiant 🙇‍♂️ ++++++\n")
            print("1.................. Voir mes cours")
            print("2........... M'inscrire à un cours")
            print("3............... Acheter du credit")
            print("4........ Passer une certification")
            print("5................. Mes certificats")
            print("6..................... Déconnexion")
            choix = input("Choisissez une option: ")
            if choix == "1":
                print("📚 Fonctionnalité en cours de développement...")
            elif choix == "2":
                CoursController.inscrire_etudiant(email)
            elif choix == "3":
                print("💵 💵 💵 💵 💵 💵 💵 💵 💵")
                PaiementController.ajouter_solde(email)
            elif choix == "4":
                CoursController.afficher_cours_diponibles()
                email = "etudiant@gmail.com"
                titre_cours = input("Entrez le titre du cours: ")
                evalCtrl.passer_quiz(email,titre_cours)
            elif choix == "5":
                email = "etudiant@gmail.com"
                certifCtrl.voir_certificats(email)
            elif choix == "6":
                print("⏼ Au revoir")
                break
            else:
                print("❌ Choix invalide")