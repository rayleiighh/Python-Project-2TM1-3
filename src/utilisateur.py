class Utilisateur:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.sets = []  # Liste de SetDeFlashcards
        self.statistiques = None  # Instance de Statistiques

    def ajouter_set(self, set_flashcards):
        self.sets.append(set_flashcards)

    def afficher_sets(self):
        if not self.sets:
            print("Aucun set de flashcards.")
        else:
            for i, set_flashcard in enumerate(self.sets, start=1):
                print(f"{i}. {set_flashcard.nom}")

    def __str__(self):
        return f"Utilisateur: {self.nom}, Email: {self.email}"
