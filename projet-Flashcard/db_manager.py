import sqlite3

class DatabaseManager:
    def __init__(self, db_name="flashcards_app.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    mot_de_passe TEXT NOT NULL
                );
            """)
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS sets_de_flashcards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    utilisateur_id INTEGER NOT NULL,
                    dernier_revision DATETIME DEFAULT NULL,
                    FOREIGN KEY(utilisateur_id) REFERENCES utilisateurs(id)
                );
            """)
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS flashcards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT NOT NULL,
                    reponse TEXT NOT NULL,
                    set_id INTEGER NOT NULL,
                    correct_count INTEGER DEFAULT 0,
                    incorrect_count INTEGER DEFAULT 0,
                    FOREIGN KEY(set_id) REFERENCES sets_de_flashcards(id)
                );
            """)
            print("Tables créées avec succès.")

    def ajouter_utilisateur(self, nom, email, mot_de_passe):
        with self.connection:
            utilisateur = self.connection.execute("""
                SELECT * FROM utilisateurs WHERE email = ?;
            """, (email,)).fetchone()

            if utilisateur:
                print(f"L'utilisateur avec l'email '{email}' existe déjà.")
                return

            self.connection.execute("""
                INSERT INTO utilisateurs (nom, email, mot_de_passe)
                VALUES (?, ?, ?);
            """, (nom, email, mot_de_passe))
            print(f"Utilisateur '{nom}' ajouté à la base de données.")

    def ajouter_set_flashcards(self, nom, utilisateur_id):
        """Ajoute un set de flashcards pour un utilisateur spécifique."""
        with self.connection:
            self.connection.execute("""
                INSERT INTO sets_de_flashcards (nom, utilisateur_id) VALUES (?, ?);
            """, (nom, utilisateur_id))

    def ajouter_flashcard(self, question, reponse, set_id):
        with self.connection:
            self.connection.execute("""
                INSERT INTO flashcards (question, reponse, set_id)
                VALUES (?, ?, ?);
            """, (question, reponse, set_id))
            print(f"Flashcard ajoutée au set ID {set_id}.")

    def obtenir_sets_pour_utilisateur(self, utilisateur_id):
        """Récupère les sets de flashcards liés à un utilisateur."""
        with self.connection:
            return self.connection.execute("""
                SELECT id, nom FROM sets_de_flashcards WHERE utilisateur_id = ?;
            """, (utilisateur_id,)).fetchall()

    def obtenir_flashcards_pour_set(self, set_id):
        with self.connection:
            return self.connection.execute("""
                SELECT * FROM flashcards
                WHERE set_id = ?;
            """, (set_id,)).fetchall()

    def obtenir_statistiques_globales(self):
        """Récupère les statistiques globales de toutes les flashcards."""
        with self.connection:
            result = self.connection.execute("""
                SELECT 
                    SUM(correct_count) AS total_correct,
                    SUM(incorrect_count) AS total_incorrect
                FROM flashcards;
            """).fetchone()

            total_correct = result["total_correct"] or 0
            total_incorrect = result["total_incorrect"] or 0
            total_reponses = total_correct + total_incorrect

            taux_reussite = (total_correct / total_reponses * 100) if total_reponses > 0 else 0
            return {
                "correct": total_correct,
                "incorrect": total_incorrect,
                "taux_reussite": taux_reussite
            }

    def obtenir_statistiques_globales(self):
        """Récupère les statistiques globales de toutes les flashcards."""
        with self.connection:
            result = self.connection.execute("""
                SELECT 
                    SUM(correct_count) AS total_correct,
                    SUM(incorrect_count) AS total_incorrect
                FROM flashcards;
            """).fetchone()

            if result:  # Vérification si la requête a renvoyé des résultats
                total_correct = result[0] or 0  # Accès par index
                total_incorrect = result[1] or 0  # Accès par index
                total_reponses = total_correct + total_incorrect

                taux_reussite = (total_correct / total_reponses * 100) if total_reponses > 0 else 0
                return {
                    "correct": total_correct,
                    "incorrect": total_incorrect,
                    "taux_reussite": taux_reussite
                }
            else:
                return {"correct": 0, "incorrect": 0, "taux_reussite": 0}

    def obtenir_statistiques_par_set(self):
        """Récupère les statistiques par set."""
        with self.connection:
            result = self.connection.execute("""
                SELECT 
                    sets_de_flashcards.nom AS set_name,
                    SUM(flashcards.correct_count) AS correct,
                    SUM(flashcards.incorrect_count) AS incorrect,
                    CASE 
                        WHEN SUM(flashcards.correct_count) + SUM(flashcards.incorrect_count) > 0
                        THEN ROUND(SUM(flashcards.correct_count) * 100.0 / (SUM(flashcards.correct_count) + SUM(flashcards.incorrect_count)), 2)
                        ELSE 0
                    END AS taux_reussite
                FROM sets_de_flashcards
                LEFT JOIN flashcards ON sets_de_flashcards.id = flashcards.set_id
                GROUP BY sets_de_flashcards.id
                ORDER BY sets_de_flashcards.nom;
            """).fetchall()

            # Organiser les résultats en tuples
            return [(row[0], row[1] or 0, row[2] or 0, row[3] or 0) for row in result]

    def modifier_flashcard(self, id, nouvelle_question, nouvelle_reponse):
        """Modifie une flashcard existante."""
        with self.connection:
            self.connection.execute("""
                UPDATE flashcards
                SET question = ?, reponse = ?
                WHERE id = ?;
            """, (nouvelle_question, nouvelle_reponse, id))

    def supprimer_flashcard(self, id):
        """Supprime une flashcard existante."""
        with self.connection:
            self.connection.execute("""
                DELETE FROM flashcards WHERE id = ?;
            """, (id,))

    def obtenir_sets_pour_utilisateur(self, utilisateur_id):
        """Récupère tous les sets de flashcards pour un utilisateur spécifique."""
        with self.connection:
            return self.connection.execute("""
                SELECT id, nom 
                FROM sets_de_flashcards
                WHERE utilisateur_id = ?
                ORDER BY nom;
            """, (utilisateur_id,)).fetchall()

    def obtenir_sets_a_reviser(self):
        """Récupère les sets qui n'ont pas été révisés depuis 24 heures."""
        with self.connection:
            return self.connection.execute("""
                SELECT id, nom, dernier_revision
                FROM sets_de_flashcards
                WHERE dernier_revision IS NULL OR dernier_revision < datetime('now', '-1 day')
                ORDER BY dernier_revision ASC;
            """).fetchall()

    def ajouter_colonne_dernier_revision(self):
        """Ajoute la colonne 'dernier_revision' à la table sets_de_flashcards si elle n'existe pas."""
        with self.connection:
            # Vérifier si la colonne existe déjà
            result = self.connection.execute("""
                PRAGMA table_info(sets_de_flashcards);
            """).fetchall()
            colonnes = [colonne[1] for colonne in result]  # Liste des noms de colonnes
            if "dernier_revision" not in colonnes:
                self.connection.execute("""
                    ALTER TABLE sets_de_flashcards ADD COLUMN dernier_revision DATETIME DEFAULT NULL;
                """)
                print("Colonne 'dernier_revision' ajoutée à la table 'sets_de_flashcards'.")
            else:
                print("Colonne 'dernier_revision' existe déjà.")

    def obtenir_utilisateurs(self):
        """Récupère tous les utilisateurs de la base de données."""
        with self.connection:
            return self.connection.execute("""
                SELECT id, nom FROM utilisateurs ORDER BY nom;
            """).fetchall()

