from db_manager import DatabaseManager
from SetDeFlashcard import SetDeFlashcards

class Utilisateur:
    def __init__(self, nom, email, mot_de_passe):
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.sets_de_flashcards = {}

    def ajouter_set_flashcards(self, set_name):
        if set_name not in self.sets_de_flashcards:
            self.sets_de_flashcards[set_name] = SetDeFlashcards(set_name)
            print(f"Set '{set_name}' ajouté pour {self.nom}.")
        else:
            print(f"Le set '{set_name}' existe déjà.")
