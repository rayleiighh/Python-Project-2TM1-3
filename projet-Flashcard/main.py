from db_manager import DatabaseManager
from statistiques import Statistiques
from SetDeFlashcard import SetDeFlashcards
from utilisateur import Utilisateur
from session_de_revision import SessionDeRevision



def main():
    db_manager = DatabaseManager()

    # Ajouter un utilisateur, un set et des flashcards (si besoin)
    db_manager.ajouter_utilisateur("Alice", "alice@example.com", "securepassword")
    db_manager.ajouter_set_flashcards("Mathématiques", 1)
    db_manager.ajouter_flashcard("2 + 2 ?", "4", 1)
    db_manager.ajouter_flashcard("3 x 3 ?", "9", 1)

    # Démarrer une session de révision
    session = SessionDeRevision(utilisateur_id=1, set_id=1, db_manager=db_manager)
    session.demarrer_session()

    # Afficher les statistiques mises à jour
    statistiques = Statistiques(utilisateur_id=1, db_manager=db_manager)
    statistiques.afficher_statistiques_globales()
    statistiques.afficher_statistiques_par_set()

if __name__ == "__main__":
    main()

