from models.evaluation import Evaluation
from controllers.certification_controller import CertificationController as certifCtrl

class EvaluationController:
    @staticmethod
    def creer_quiz() -> None:
        titre_cours = input("Titre du cours : ")
        questions = []

        while True:
            question = input("Question : ")
            option_a = input("Option A : ")
            option_b = input("Option B : ")
            option_c = input("Option C : ")
            reponse = input("Réponse correcte (A/B/C) : ").upper()

            questions.append({
                "question": question,
                "options": {
                    "A": option_a,
                    "B": option_b,
                    "C": option_c
                },
                "reponse": reponse
            })
            continuer = input("Ajouter une autre question? (O/N) : ").upper()
            if continuer == "N":
                break

        quiz = Evaluation(titre_cours, questions)
        quiz.sauvegarder()
        print(f"✅ Quiz pour le cours '{titre_cours}' créé avec succès !")

    @staticmethod
    def passer_quiz(email_etudiant,titre_cours: str) -> None:
        evaluation = Evaluation.obtenir_evaluation(titre_cours)
        if evaluation is None:
            print(f"❌ Aucun quiz trouvé pour le cours '{titre_cours}'.")
            return

        print(f"====> 📝 Quiz pour le cours'{titre_cours}' 📝 <====")
        score = 0
        questions = evaluation['questions']
        for i,q in enumerate(questions, start=1):
            print(f"{i}) {q['question']}")
            for key, value in q['options'].items():
                print(f"{key}. {value}")
            reponse_etudiant = input("Votre réponse : ").upper()
            if reponse_etudiant == q['reponse']:
                score += 1
        
        total_questions = len(questions)
        poucentage = (score / total_questions) * 100
        print(f"📝 Score : {score}/{total_questions} ({poucentage:.2f}%)")
        if poucentage >= 70:
            print("🎉 Félicitations ! Vous recevez un certificat 📜 pour ce cours!")
            certifCtrl.generer_certificat(email_etudiant, titre_cours)
        else:
            print("😞 Vous n'avez pas réussi le quiz. Révisez les cours et réessayez !")