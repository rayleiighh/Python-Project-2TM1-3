from flashcard import Flashcard




class SetDeFlashcards:
    def __init__(self, nom):
        self.nom = nom
        self.liste_flashcards = []

    def ajouter_flashcard(self, question, reponse):
        self.liste_flashcards.append(Flashcard(question, reponse))
        print(f"Flashcard ajoutée au set '{self.nom}'.")

    def lister_flashcards(self):
        for i, card in enumerate(self.liste_flashcards, start=1):
            print(f"{i}. {card.afficher_question()}")
