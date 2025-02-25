from database.db import db
from tinydb import Query
class CertificationController:
    @staticmethod
    def generer_certificat(email_etudiant, titre_cours):
        certif_table = db.table('certifications')
        certif_table.insert({
            'email_etudiant': email_etudiant, 
            'titre_cours': titre_cours
        })
        print("📜 Certificat enregister avec succès !")
        
    @staticmethod
    def voir_certificats(email_etudiant):
        certif_table = db.table('certifications')
        certificats = certif_table.search(Query().email_etudiant == email_etudiant)

        if not certificats:
            print("❌ Aucun certificat trouvé.")
            return
        print("\n=======> Mes Certificats 🧑‍🎓 📜 👨‍🎓 <=======")
        for i, certif in enumerate(certificats,start=1):
            print(f"{i}. {certif['titre_cours']}📜")