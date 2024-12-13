import unittest
from utilisateur import Utilisateur
from recompense import Recompense

class TestRecompense(unittest.TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur("Test User", "test@example.com", "password123")
        self.recompense = Recompense(1, "Reward", "Description", "condition", self.utilisateur)

    def test_verifier_condition(self):
        historique = ["condition"]
        self.assertTrue(self.recompense.verifier_condition(historique))
        self.assertFalse(self.recompense.verifier_condition([]))

    def test_debloquer(self):
        historique = ["condition"]
        self.assertTrue(self.recompense.debloquer(historique))
        with self.assertRaises(PermissionError):
            self.recompense.debloquer([])


if __name__ == "__main__":
    unittest.main()
