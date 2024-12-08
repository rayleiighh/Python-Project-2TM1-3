class SetDeFlashcards:
    def __init__(self, nom):
        self.nom = nom
        self.flashcards = []  # Liste de Flashcards

    def ajouter_flashcard(self, flashcard):
        self.flashcards.append(flashcard)

    def afficher_flashcards(self):
        if not self.flashcards:
            print("Aucune flashcard.")
        else:
            for i, flashcard in enumerate(self.flashcards, start=1):
                print(f"{i}. Question: {flashcard.question}, Réponse: {flashcard.reponse}")

    def __str__(self):
        return f"Set: {self.nom}, {len(self.flashcards)} flashcards"
