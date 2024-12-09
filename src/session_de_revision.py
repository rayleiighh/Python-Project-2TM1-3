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
        self.en_cours = True
        self.debut = time.time()
        self.bonnes_reponses = 0
        self.mauvaises_reponses = 0
        print(f"Session démarrée pour le set : {self.set.nom}")

    def terminer_session(self) -> None:
        """Termine la session de révision en enregistrant les résultats."""
        if not self.en_cours:
            raise RuntimeError("Aucune session n'est en cours.")
        self.en_cours = False
        self.fin = time.time()
        print("Session terminée.")

    def afficher_statistiques(self) -> dict:
        """Retourne un dictionnaire contenant les statistiques de la session."""
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

    def repondre_a_flashcard(self, flashcard: Flashcard, reponse_utilisateur: str) -> None:
        """Permet à l'utilisateur de répondre à une flashcard et enregistre le résultat."""
        if not self.en_cours:
            raise RuntimeError("Aucune session n'est en cours.")
        if reponse_utilisateur.lower() == flashcard.reponse.lower():
            self.bonnes_reponses += 1
            print("Bonne réponse !")
        else:
            self.mauvaises_reponses += 1
            print(f"Mauvaise réponse. La bonne réponse est : {flashcard.reponse}")
