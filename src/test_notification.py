import unittest
import datetime
from utilisateur import Utilisateur
from notification import Notification


class TestNotification(unittest.TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur("Test User", "test@example.com", "password123")
        self.notification = Notification(1, "info", "Ceci est un test", self.utilisateur)

    def test_envoyer(self):
        self.assertTrue(self.notification.envoyer())
        self.notification.contenu = ""
        with self.assertRaises(ValueError):
            self.notification.envoyer()

    def test_planifier(self):
        date_valide = datetime.datetime.now() + datetime.timedelta(days=1)
        self.assertTrue(self.notification.planifier(date_valide))
        date_invalide = datetime.datetime.now() - datetime.timedelta(days=1)
        with self.assertRaises(ValueError):
            self.notification.planifier(date_invalide)

if __name__ == "__main__":
    unittest.main()
