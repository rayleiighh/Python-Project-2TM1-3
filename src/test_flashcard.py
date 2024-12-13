import unittest
from flashcard import Flashcard


class TestFlashcard(unittest.TestCase):

    def test_afficher_question_valide(self):
        flashcard = Flashcard("Quelle est la capitale de la France ?", "Paris")
        self.assertEqual(flashcard.afficher_question(), "Quelle est la capitale de la France ?")

    def test_afficher_question_vide(self):
        flashcard = Flashcard("Quelle est la capitale de la France ?", "Paris")
        flashcard.question = ""  # Simule un changement de l'état
        with self.assertRaises(ValueError):
            flashcard.afficher_question()

    def test_afficher_question_none(self):
        flashcard = Flashcard("Quelle est la capitale de la France ?", "Paris")
        flashcard.question = None  # Simule un changement de l'état
        with self.assertRaises(ValueError):
            flashcard.afficher_question()

    def test_afficher_reponse_valide(self):
        flashcard = Flashcard("Quelle est la capitale de la France ?", "Paris")
        self.assertEqual(flashcard.afficher_reponse(), "Paris")

    def test_afficher_reponse_vide(self):
        flashcard = Flashcard("Quelle est la capitale de la France ?", "Paris")
        flashcard.reponse = ""  # Simule un changement de l'état
        with self.assertRaises(ValueError):
            flashcard.afficher_reponse()

    def test_afficher_reponse_none(self):
        flashcard = Flashcard("Quelle est la capitale de la France ?", "Paris")
        flashcard.reponse = None  # Simule un changement de l'état
        with self.assertRaises(ValueError):
            flashcard.afficher_reponse()


if __name__ == '__main__':
    unittest.main()
