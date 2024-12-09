#Incrémenté par Rayane
class Flashcard:
    def __init__(self, question: str, reponse: str, flashcard_id=None):
        if not question or not reponse:
            raise ValueError("La question et la réponse doivent être non vides.")
        self.id = flashcard_id  # Optionnel, défini lors de la récupération depuis la DB
        self.question = question
        self.reponse = reponse

    def afficher_question(self) -> str:
        """Retourne la question de la flashcard."""
        if not self.question:
            raise ValueError("La question de la flashcard est vide.")
        return self.question

    def afficher_reponse(self) -> str:
        """Retourne la réponse de la flashcard."""
        if not self.reponse:
            raise ValueError("La réponse de la flashcard est vide.")
        return self.reponse
