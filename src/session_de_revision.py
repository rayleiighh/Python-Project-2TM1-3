#Incrémenté par Rayane
import time
from flashcard import Flashcard
from set_de_flashcard import SetDeFlashcards

class SessionDeRevision:
    def __init__(self, set_de_flashcards: SetDeFlashcards):
        self.set = set_de_flashcards
        self.en_cours = False
        self.debut = None
        self.fin = None
        self.bonnes_reponses = 0
        self.mauvaises_reponses = 0

    def demarrer_session(self) -> None:
        """Démarre une session de révision en initialisant les paramètres nécessaires."""
        if self.en_cours:
            raise RuntimeError("Une session est déjà en cours.")
        if not hasattr(self.set, "nom") or not isinstance(self.set.nom, str):
            raise ValueError("Le set fourni est invalide ou n'a pas de nom.")
        if not self.set.flashcards:
            raise ValueError("Le set ne contient aucune flashcard à réviser.")
        self.en_cours = True
        self.debut = time.time()
        self.bonnes_reponses = 0
        self.mauvaises_reponses = 0
        print(f"Session démarrée pour le set : {self.set.nom}")

    def repondre_a_flashcard(self, flashcard, reponse_utilisateur: str) -> None:
        """Permet de répondre à une flashcard et met à jour les statistiques."""
        if not self.en_cours:
            raise RuntimeError("Aucune session en cours.")
        if reponse_utilisateur.strip().lower() == flashcard.reponse.strip().lower():
            print("Bonne réponse !")
            self.bonnes_reponses += 1
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {flashcard.reponse}")
            self.mauvaises_reponses += 1

    def terminer_session(self, stats_manager, utilisateur_id: int) -> None:
        """Termine la session, affiche les résultats et met à jour les statistiques de l'utilisateur."""
        if not self.en_cours:
            raise RuntimeError("Aucune session en cours.")
        self.en_cours = False
        self.fin = time.time()
        print(f"Session terminée pour le set : {self.set.nom}")
        print("Session terminée ! Voici vos statistiques :")
        print(f"Cartes révisées : {self.bonnes_reponses + self.mauvaises_reponses}")
        print(f"Bonnes réponses : {self.bonnes_reponses}")
        pourcentage_reussite = (self.bonnes_reponses / (self.bonnes_reponses + self.mauvaises_reponses)) * 100
        print(f"Pourcentage de réussite : {pourcentage_reussite:.2f}%")

        # Mettre à jour les statistiques de l'utilisateur via StatistiquesManager
        try:
            stats = stats_manager.get_statistiques(utilisateur_id)
            stats.bonnes_reponses += self.bonnes_reponses
            stats.cartes_revisees += (self.bonnes_reponses + self.mauvaises_reponses)
            stats_manager.update_statistiques(stats)
        except ValueError as e:
            print(f"Erreur : {e}. Les statistiques n'ont pas pu être mises à jour.")

    def afficher_statistiques(self) -> dict:
        """Retourne les statistiques de la session."""
        if self.en_cours:
            raise RuntimeError("La session est toujours en cours.")
        duree = self.fin - self.debut if self.fin and self.debut else 0
        total_questions = self.bonnes_reponses + self.mauvaises_reponses
        taux_reussite = (self.bonnes_reponses / total_questions * 100) if total_questions > 0 else 0
        return {
            "cartes_revisees": total_questions,
            "bonnes_reponses": self.bonnes_reponses,
            "pourcentage_reussite": taux_reussite,
            "duree_session": duree
        }
