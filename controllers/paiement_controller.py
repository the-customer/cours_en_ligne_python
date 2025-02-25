from models.paiement import Paiement
class PaiementController:
    @staticmethod
    def ajouter_solde(email: str) -> None:
        montant = int(input("Entrer le montant à acheter : "))
        paiement = Paiement(email,montant)
        paiement.enregistrer_paiement_credit()