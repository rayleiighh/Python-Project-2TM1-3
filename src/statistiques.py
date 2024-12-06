from db_manager import DatabaseManager



class Statistiques:
    def __init__(self, utilisateur_id: int, db_manager: DatabaseManager):
        self.utilisateur_id = utilisateur_id
        self.db_manager = db_manager

    def calculer_taux_reussite(self):
        sets = self.db_manager.obtenir_sets_pour_utilisateur(self.utilisateur_id)
        total_correct = 0
        total_incorrect = 0

        for set_ in sets:
            set_id = set_[0]
            flashcards = self.db_manager.obtenir_flashcards_pour_set(set_id)
            for card in flashcards:
                total_correct += card[4]
                total_incorrect += card[5]

        total_attempts = total_correct + total_incorrect
        if total_attempts > 0:
            return (total_correct / total_attempts) * 100
        return 0.0

    def afficher_statistiques_globales(self):
        taux_reussite = self.calculer_taux_reussite()
        print(f"Taux de réussite global: {taux_reussite:.2f}%")

    def afficher_statistiques_par_set(self):
        sets = self.db_manager.obtenir_sets_pour_utilisateur(self.utilisateur_id)
        for set_ in sets:
            set_id, set_nom, _ = set_
            flashcards = self.db_manager.obtenir_flashcards_pour_set(set_id)
            total_correct = sum(card[4] for card in flashcards)
            total_incorrect = sum(card[5] for card in flashcards)
            total_attempts = total_correct + total_incorrect
            taux_reussite = (total_correct / total_attempts) * 100 if total_attempts > 0 else 0.0
            print(f"Set '{set_nom}': Taux de réussite: {taux_reussite:.2f}%")
