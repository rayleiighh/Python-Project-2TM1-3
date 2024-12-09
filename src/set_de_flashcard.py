#Incrémenté par Rayane
from flashcard import Flashcard


class SetDeFlashcards:
    def __init__(self, nom: str, set_id=None):
        if not nom:
            raise ValueError("Le nom du set ne peut pas être vide.")
        self.id = set_id  # Optionnel, défini lors de la récupération depuis la DB
        self.nom = nom
        self.flashcards = []  # Liste de flashcards

    def ajouter_flashcard(self, flashcard: Flashcard) -> None:
        """Ajoute une flashcard au set de flashcards."""
        if any(fc.question == flashcard.question for fc in self.flashcards):
            raise ValueError("Une flashcard avec cette question existe déjà dans le set.")
        self.flashcards.append(flashcard)

    def supprimer_flashcard(self, flashcard_id: int) -> None:
        """Supprime une flashcard du set en fonction de son identifiant."""
        flashcard = next((fc for fc in self.flashcards if fc.id == flashcard_id), None)
        if not flashcard:
            raise LookupError("Flashcard avec cet identifiant introuvable.")
        self.flashcards.remove(flashcard)

    def modifier_flashcard(self, flashcard_id: int, nouvelle_question: str, nouvelle_reponse: str) -> None:
        """Modifie la question et la réponse d'une flashcard existante."""
        flashcard = next((fc for fc in self.flashcards if fc.id == flashcard_id), None)
        if not flashcard:
            raise LookupError("Flashcard avec cet identifiant introuvable.")
        if not nouvelle_question or not nouvelle_reponse:
            raise ValueError("La nouvelle question et la nouvelle réponse doivent être non vides.")
        flashcard.question = nouvelle_question
        flashcard.reponse = nouvelle_reponse
