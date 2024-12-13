import unittest
from utilisateur import Utilisateur


class TestUtilisateur(unittest.TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur("Test User", "test@example.com", "password123")

    def test_email_validation(self):
        with self.assertRaises(ValueError):
            Utilisateur("User", "invalidemail", "password123")

    def test_password_validation(self):
        with self.assertRaises(ValueError):
            Utilisateur("User", "valid@example.com", "short")

    def test_se_connecter(self):
        self.assertTrue(self.utilisateur.se_connecter("test@example.com", "password123"))
        self.assertFalse(self.utilisateur.se_connecter("wrong@example.com", "password123"))

    def test_se_deconnecter(self):
        self.utilisateur.se_connecter("test@example.com", "password123")
        self.assertTrue(self.utilisateur.se_deconnecter())
        self.assertFalse(self.utilisateur.se_deconnecter())


if __name__ == "__main__":
    unittest.main()
