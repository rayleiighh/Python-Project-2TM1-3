class Flashcard:
    def afficher_question(self) -> str:
        """
        Retourne la question de la flashcard.

        PRE :
            - La flashcard a été correctement initialisée.
            - La question n'est pas vide et n'est pas None.
        POST :
            - Retourne une chaîne de caractères représentant la question.
        RAISES :
            - ValueError : Si la question est vide ou None.
        """
        pass

    def afficher_reponse(self) -> str:
        """
        Retourne la réponse de la flashcard.

        PRE :
            - La flashcard a été correctement initialisée.
            - La réponse n'est pas vide et n'est pas None.
        POST :
            - Retourne une chaîne de caractères représentant la réponse.
        RAISES :
            - ValueError : Si la réponse est vide ou None.
        """
        pass


class SetDeFlashcards:
    def ajouter_flashcard(self, flashcard) -> None:
        """
        Ajoute une flashcard au set de flashcards.

        PRE :
            - flashcard est une instance de Flashcard.
            - La question de la flashcard n'existe pas déjà dans le set.
        POST :
            - La flashcard est ajoutée au set.
        RAISES :
            - ValueError : Si une flashcard avec la même question existe déjà dans le set.
        """
        pass

    def supprimer_flashcard(self, flashcard_id: int) -> None:
        """
        Supprime une flashcard du set en fonction de son identifiant.

        PRE :
            - flashcard_id est un entier positif.
            - Une flashcard avec cet identifiant existe dans le set.
        POST :
            - La flashcard correspondant à l'identifiant est supprimée.
        RAISES :
            - LookupError : Si aucune flashcard avec l'identifiant fourni n'est trouvée.
        """
        pass

    def modifier_flashcard(self, flashcard_id: int, nouvelle_question: str, nouvelle_reponse: str) -> None:
        """
        Modifie la question et la réponse d'une flashcard existante.

        PRE :
            - flashcard_id est un entier positif.
            - Une flashcard avec cet identifiant existe dans le set.
            - nouvelle_question et nouvelle_reponse sont des chaînes non vides.
        POST :
            - La question et la réponse de la flashcard sont mises à jour.
        RAISES :
            - LookupError : Si aucune flashcard avec l'identifiant fourni n'est trouvée.
        """
        pass


class SessionDeRevision:
    def demarrer_session(self) -> None:
        """
        Démarre une session de révision en initialisant les paramètres nécessaires.

        PRE :
            - Aucune autre session n'est en cours.
        POST :
            - Une nouvelle session de révision est initialisée.
        RAISES :
            - RuntimeError : Si une session est déjà en cours.
        """
        pass

    def terminer_session(self) -> None:
        """
        Termine la session de révision en enregistrant les résultats.

        PRE :
            - Une session de révision est en cours.
        POST :
            - La session de révision est terminée et les résultats sont sauvegardés.
        RAISES :
            - RuntimeError : Si aucune session n'a été démarrée.
        """
        pass

    def afficher_statistiques(self) -> dict:
        """
        Retourne un dictionnaire contenant les statistiques de la session.

        PRE :
            - La session de révision est terminée.
        POST :
            - Retourne un dictionnaire contenant :
                - Le nombre de cartes révisées.
                - Le nombre de bonnes réponses.
                - Le pourcentage de réussite.
                - La durée de la session.
        RAISES :
            - RuntimeError : Si la session n'est pas encore terminée.
        """
        pass
