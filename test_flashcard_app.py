import unittest
from tkinter import Tk, messagebox
from flashcard_app import FlashcardApp
from db_manager import DatabaseManager
from unittest.mock import patch

class TestFlashcardApp(unittest.TestCase):
    def setUp(self):
        """Initialise une instance de FlashcardApp et une base de données en mémoire."""
        self.db_manager = DatabaseManager(":memory:")  # Base de données temporaire en mémoire
        self.db_manager.create_tables()  # Crée les tables nécessaires
        self.root = Tk()
        self.app = FlashcardApp(self.root, self.db_manager)

    def tearDown(self):
        """Ferme la fenêtre Tkinter après les tests."""
        self.root.destroy()

    @patch("tkinter.messagebox.showerror")
    def test_require_active_user(self, mock_showerror):
        """Teste le comportement des méthodes décorées sans utilisateur actif."""
        self.app.utilisateur_actif = None  # Aucun utilisateur actif

        # Appelle une méthode nécessitant un utilisateur actif
        self.app.ajouter_flashcard()

        # Vérifie que le message d'erreur est affiché
        mock_showerror.assert_called_once_with(
            "Erreur", "Veuillez d'abord sélectionner un utilisateur."
        )

    def test_active_user_behavior(self):
        """Teste le comportement des méthodes décorées avec un utilisateur actif."""
        # Ajout d'un utilisateur dans la base de données
        self.db_manager.ajouter_utilisateur("TestUser", "test@example.com", "password123")
        utilisateurs = self.db_manager.obtenir_utilisateurs()
        self.app.utilisateur_actif = utilisateurs[0][0]  # Sélectionne l'utilisateur ajouté

        try:
            self.app.ajouter_flashcard()  # Appelle la méthode avec un utilisateur actif
            self.assertTrue(True)  # Si aucune erreur, le test passe
        except Exception:
            self.fail("La méthode ne devrait pas lever d'exception avec un utilisateur actif.")

if __name__ == "__main__":
    unittest.main()
