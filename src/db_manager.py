#Incrémenté par Rayane
import sqlite3
from flashcard import Flashcard
from set_de_flashcard import SetDeFlashcards


class DatabaseManager:
    def __init__(self, db_name="flashcard_app.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Crée les tables nécessaires dans la base de données."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                );
            """)
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS sets_de_flashcards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    utilisateur_id INTEGER NOT NULL,
                    FOREIGN KEY(utilisateur_id) REFERENCES utilisateurs(id)
                );
            """)
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS flashcards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT NOT NULL,
                    reponse TEXT NOT NULL,
                    set_id INTEGER NOT NULL,
                    FOREIGN KEY(set_id) REFERENCES sets_de_flashcards(id)
                );
            """)

    def ajouter_utilisateur(self, nom, email):
        """Ajoute un utilisateur à la base de données."""
        with self.connection:
            self.connection.execute("""
                INSERT INTO utilisateurs (nom, email) VALUES (?, ?);
            """, (nom, email))

    def obtenir_utilisateurs(self):
        """Récupère tous les utilisateurs."""
        with self.connection:
            return self.connection.execute("""
                SELECT id, nom, email FROM utilisateurs;
            """).fetchall()

    def ajouter_set(self, nom, utilisateur_id):
        """Ajoute un set de flashcards à un utilisateur."""
        with self.connection:
            self.connection.execute("""
                INSERT INTO sets_de_flashcards (nom, utilisateur_id) VALUES (?, ?);
            """, (nom, utilisateur_id))

    def obtenir_sets(self, utilisateur_id):
        """Récupère les sets d'un utilisateur."""
        with self.connection:
            return self.connection.execute("""
                SELECT id, nom FROM sets_de_flashcards WHERE utilisateur_id = ?;
            """, (utilisateur_id,)).fetchall()

    def ajouter_flashcard(self, question, reponse, set_id):
        """Ajoute une flashcard à un set."""
        with self.connection:
            self.connection.execute("""
                INSERT INTO flashcards (question, reponse, set_id) VALUES (?, ?, ?);
            """, (question, reponse, set_id))

    def obtenir_flashcards(self, set_id):
        """Récupère les flashcards d'un set."""
        with self.connection:
            return self.connection.execute("""
                SELECT id, question, reponse FROM flashcards WHERE set_id = ?;
            """, (set_id,)).fetchall()

    def obtenir_set_de_flashcards(self, set_id: int):
        """Récupère un set de flashcards depuis la base de données."""
        result = self.connection.execute("""
            SELECT nom FROM sets_de_flashcards WHERE id = ?;
        """, (set_id,)).fetchone()
        if result:
            set_flashcards = SetDeFlashcards(result[0], set_id)
            flashcards = self.obtenir_flashcards(set_id)
            for fc in flashcards:
                set_flashcards.ajouter_flashcard(Flashcard(fc[1], fc[2], fc[0]))
            return set_flashcards
        else:
            raise LookupError("Set introuvable.")

    def sauvegarder_flashcard(self, flashcard: Flashcard, set_id: int):
        """Sauvegarde une flashcard dans la base de données."""
        with self.connection:
            if flashcard.id:
                self.connection.execute("""
                    UPDATE flashcards SET question = ?, reponse = ? WHERE id = ?;
                """, (flashcard.question, flashcard.reponse, flashcard.id))
            else:
                self.connection.execute("""
                    INSERT INTO flashcards (question, reponse, set_id) VALUES (?, ?, ?);
                """, (flashcard.question, flashcard.reponse, set_id))
