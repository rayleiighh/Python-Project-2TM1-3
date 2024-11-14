class Flashcard:
    def afficher_question(self) -> str:
        """
        Retourne la question de la flashcard.
        
        Exceptions :
        - ValueError : Si la question est vide ou None.
        """
        pass

    def afficher_reponse(self) -> str:
        """
        Retourne la réponse de la flashcard.
        
        Exceptions :
        - ValueError : Si la réponse est vide ou None.
        """
        pass


class SetDeFlashcards:
    def ajouter_flashcard(self, flashcard) -> None:
        """
        Ajoute une flashcard au set de flashcards.
        
        Paramètres :
        - flashcard : Flashcard, la flashcard à ajouter.
        
        Exceptions :
        - ValueError : Si une flashcard avec la même question existe déjà dans le set.
        """
        pass

    def supprimer_flashcard(self, flashcard_id: int) -> None:
        """
        Supprime une flashcard du set en fonction de son identifiant.
        
        Paramètres :
        - flashcard_id : int, l'identifiant de la flashcard à supprimer.
        
        Exceptions :
        - LookupError : Si aucune flashcard avec l'identifiant fourni n'est trouvée.
        """
        pass

    def modifier_flashcard(self, flashcard_id: int, nouvelle_question: str, nouvelle_reponse: str) -> None:
        """
        Modifie la question et la réponse d'une flashcard existante.
        
        Paramètres :
        - flashcard_id : int, l'identifiant de la flashcard à modifier.
        - nouvelle_question : str, la nouvelle question.
        - nouvelle_reponse : str, la nouvelle réponse.
        
        Exceptions :
        - LookupError : Si aucune flashcard avec l'identifiant fourni n'est trouvée.
        """
        pass


class SessionDeRevision:
    def demarrer_session(self) -> None:
        """
        Démarre une session de révision en initialisant les paramètres nécessaires.
        
        Exceptions :
        - RuntimeError : Si une session est déjà en cours.
        """
        pass

    def terminer_session(self) -> None:
        """
        Termine la session de révision en enregistrant les résultats.
        
        Exceptions :
        - RuntimeError : Si aucune session n'a été démarrée.
        """
        pass

    def afficher_statistiques(self) -> dict:
        """
        Retourne un dictionnaire contenant les statistiques de la session.
        
        Retour :
        - dict : Dictionnaire avec le nombre de cartes révisées, le nombre de bonnes réponses, le pourcentage de réussite et la durée.
        
        Exceptions :
        - RuntimeError : Si la session n'est pas encore terminée.
        """
        pass
