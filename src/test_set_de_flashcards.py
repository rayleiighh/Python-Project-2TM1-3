import unittest
from flashcard import Flashcard
from set_de_flashcard import SetDeFlashcards


class TestSetDeFlashcards(unittest.TestCase):

    def setUp(self):
        """Configuration initiale avant chaque test."""
        self.set_flashcards = SetDeFlashcards("MonSet")
        self.flashcard1 = Flashcard("Quelle est la capitale de la France ?", "Paris")
        self.flashcard2 = Flashcard("Quelle est la capitale de l'Allemagne ?", "Berlin")

    def test_ajouter_flashcard_valide(self):
        self.set_flashcards.ajouter_flashcard(self.flashcard1)
        self.assertIn(self.flashcard1, self.set_flashcards.flashcards)

    def test_ajouter_flashcard_doublon(self):
        self.set_flashcards.ajouter_flashcard(self.flashcard1)
        with self.assertRaises(ValueError):
            self.set_flashcards.ajouter_flashcard(self.flashcard1)

    def test_supprimer_flashcard_valide(self):
        self.set_flashcards.ajouter_flashcard(self.flashcard1)
        self.set_flashcards.supprimer_flashcard(self.flashcard1)
        self.assertNotIn(self.flashcard1, self.set_flashcards.flashcards)

    def test_supprimer_flashcard_inexistante(self):
        with self.assertRaises(ValueError):
            self.set_flashcards.supprimer_flashcard(self.flashcard1)

    def test_modifier_flashcard_valide(self):
        self.set_flashcards.ajouter_flashcard(self.flashcard1)
        self.set_flashcards.modifier_flashcard(self.flashcard1, "Nouvelle question ?", "Nouvelle réponse.")
        self.assertEqual(self.flashcard1.question, "Nouvelle question ?")
        self.assertEqual(self.flashcard1.reponse, "Nouvelle réponse.")

    def test_modifier_flashcard_inexistante(self):
        with self.assertRaises(ValueError):
            self.set_flashcards.modifier_flashcard(self.flashcard1, "Nouvelle question ?", "Nouvelle réponse.")

    def test_modifier_flashcard_champs_vides(self):
        self.set_flashcards.ajouter_flashcard(self.flashcard1)
        with self.assertRaises(ValueError):
            self.set_flashcards.modifier_flashcard(self.flashcard1, "", "Nouvelle réponse.")
        with self.assertRaises(ValueError):
            self.set_flashcards.modifier_flashcard(self.flashcard1, "Nouvelle question ?", "")


if __name__ == '__main__':
    unittest.main()
