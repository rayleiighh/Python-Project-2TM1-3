from db_manager import DatabaseManager


class SessionDeRevision:
    """Classe représentant une session de révision."""
    def __init__(self, utilisateur_id: int, set_id: int, db_manager: DatabaseManager):
        self.utilisateur_id = utilisateur_id
        self.set_id = set_id
        self.db_manager = db_manager
        self.cartes_revisees = 0
        self.bonnes_reponses = 0

    def demarrer_session(self):
        """Démarre une session de révision et enregistre les performances."""
        flashcards = self.db_manager.obtenir_flashcards_pour_set(self.set_id)
        for card in flashcards:
            question, reponse, correct_count, incorrect_count = card[1], card[2], card[4], card[5]
            print(f"Question: {question}")
            user_reponse = input("Votre réponse: ").strip()

            if user_reponse.lower() == reponse.lower():
                print("Correct!")
                self.bonnes_reponses += 1
                correct_count += 1
            else:
                print(f"Incorrect. La bonne réponse est: {reponse}")
                incorrect_count += 1

            self.cartes_revisees += 1
            # Mise à jour des performances dans la base de données
            self.db_manager.connection.execute("""
                UPDATE flashcards
                SET correct_count = ?, incorrect_count = ?
                WHERE id = ?;
            """, (correct_count, incorrect_count, card[0]))

        # Afficher les résultats de la session
        self.afficher_statistiques()

    def afficher_statistiques(self):
        """Affiche les résultats de la session."""
        print("Statistiques de la session:")
        print(f"Cartes révisées: {self.cartes_revisees}")
        print(f"Bonnes réponses: {self.bonnes_reponses}")
        if self.cartes_revisees > 0:
            taux_reussite = (self.bonnes_reponses / self.cartes_revisees) * 100
            print(f"Taux de réussite: {taux_reussite:.2f}%")

