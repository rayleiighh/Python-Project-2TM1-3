import time

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.next_review = time.time()  # Initialisé pour révision immédiate
        self.correct_count = 0
        self.incorrect_count = 0

    def review(self):
        """Permet de revoir la flashcard et d'entrer une réponse"""
        print(f"Question: {self.question}")
        user_answer = input("Votre réponse: ").strip()  # Supprime les espaces superflus
        if user_answer.lower() == self.answer.lower():
            print("Correct!")
            self.correct_count += 1
            self.schedule_next_review(True)
        else:
            print(f"Incorrect. La bonne réponse est: {self.answer}")
            self.incorrect_count += 1
            self.schedule_next_review(False)

    def schedule_next_review(self, was_correct):
        """Calcule le prochain moment de révision basé sur la performance"""
        if was_correct:
            # Espacement plus grand si correct
            self.next_review = time.time() + (60 * (self.correct_count + 1))  # Exemple: espacement d'1 min par succès
        else:
            # Révision plus rapprochée si incorrect
            self.next_review = time.time() + 30  # Révision dans 30 secondes en cas d'erreur

class FlashcardApp:
    def __init__(self):
        self.sets = {}

    def create_flashcard_set(self, set_name):
        """Créer un set et y ajouter plusieurs flashcards"""
        set_name = set_name.strip()  # Supprime les espaces autour du nom du set
        if set_name not in self.sets:
            self.sets[set_name] = []
        
        print(f"Ajoutez des flashcards dans le set '{set_name}'.")
        while True:
            question = input("Entrez la question (ou tapez 'stop' pour arrêter): ").strip()
            if question.lower() == 'stop':
                break
            answer = input("Entrez la réponse: ").strip()
            card = Flashcard(question, answer)
            self.sets[set_name].append(card)
            print("Flashcard ajoutée.")
        
        print(f"Set '{set_name}' créé avec {len(self.sets[set_name])} flashcards.")

    def add_question_to_set(self, set_name):
        """Ajouter une question à un set existant"""
        set_name = set_name.strip()  # Supprime les espaces autour du nom du set
        if set_name not in self.sets:
            print(f"Set '{set_name}' introuvable.")
            return
        
        question = input("Entrez la question à ajouter: ").strip()
        answer = input("Entrez la réponse: ").strip()
        card = Flashcard(question, answer)
        self.sets[set_name].append(card)
        print(f"Flashcard ajoutée au set '{set_name}'.")

    def review_set(self, set_name):
        """Permet de revoir un set spécifique"""
        set_name = set_name.strip()  # Supprime les espaces autour du nom du set
        if set_name not in self.sets:
            print(f"Set '{set_name}' introuvable.")
            return
        print(f"Révision du set '{set_name}'")
        
        # Révision répétée du set jusqu'à ce que l'utilisateur décide de quitter
        while True:
            for card in self.sets[set_name]:
                card.review()
            
            # Demander si l'utilisateur veut continuer la révision du set
            continue_review = input("Voulez-vous réviser ce set à nouveau ? (oui/non): ").strip().lower()
            if continue_review != "oui":
                print("Fin de la révision pour ce set.")
                break

    def show_progress(self, set_name):
        """Affiche les statistiques d'un set"""
        set_name = set_name.strip()  # Supprime les espaces autour du nom du set
        if set_name not in self.sets:
            print(f"Set '{set_name}' introuvable.")
            return
        correct = sum(card.correct_count for card in self.sets[set_name])
        incorrect = sum(card.incorrect_count for card in self.sets[set_name])
        total = correct + incorrect
        print(f"Progression du set '{set_name}':")
        print(f"  Correct: {correct}")
        print(f"  Incorrect: {incorrect}")
        print(f"  Taux de réussite: {correct / total * 100 if total > 0 else 0:.2f}%")

    def list_sets(self):
        """Liste tous les sets disponibles"""
        if not self.sets:
            print("Aucun set disponible.")
        else:
            print("Sets disponibles:")
            for set_name in self.sets:
                print(f"  - {set_name}")

def main():
    app = FlashcardApp()
    print("Bienvenue dans l'application de flashcards !")

    while True:
        print("\nOptions:")
        print("1. Créer un set et ajouter des flashcards")
        print("2. Ajouter une question à un set existant")
        print("3. Réviser un set")
        print("4. Afficher la progression d'un set")
        print("5. Afficher tous les sets")
        print("6. Quitter")
        
        choice = input("Choisissez une option: ")
        
        if choice == "1":
            set_name = input("Nom du set: ")
            app.create_flashcard_set(set_name)
        
        elif choice == "2":
            set_name = input("Nom du set auquel ajouter une question: ")
            app.add_question_to_set(set_name)
        
        elif choice == "3":
            set_name = input("Nom du set à réviser: ")
            app.review_set(set_name)
        
        elif choice == "4":
            set_name = input("Nom du set pour voir la progression: ")
            app.show_progress(set_name)
        
        elif choice == "5":
            app.list_sets()
        
        elif choice == "6":
            print("Merci d'avoir utilisé l'application de flashcards. À bientôt!")
            break
        
        else:
            print("Option non reconnue, veuillez réessayer.")

if __name__ == "__main__":
    main()