class Utilisateur:
    
    def se_connecter(self):
        """
        Authentifie l'utilisateur avec les informations fournies.

        PRE:
        - Les informations nécessaires à l'authentification (ex. nom d'utilisateur, mot de passe) doivent être fournies.
        - Les informations doivent être valides (type et format conformes).

        POST:
        - Retourne True si la session est active.
        - Retourne False si l'authentification a échoué.

        RAISES:
        - ValueError: Si des informations requises sont manquantes ou invalides.
        - ConnectionError: Si une erreur technique survient lors de la connexion.
        """
        pass

    def se_deconnecter(self):
        """
        Termine la session utilisateur en actualisant l'état de connexion.

        PRE:
        - Une session utilisateur doit être active.

        POST:
        - Retourne True si la session est fermée avec succès.
        - Retourne False si la déconnexion échoue.

        RAISES:
        - RuntimeError: Si aucune session n’est active.
        """
        pass

    def mettre_a_jour_profil(self):
        """
        Permet à l'utilisateur de modifier et sauvegarder ses informations de profil.

        PRE:
        - L'utilisateur doit être authentifié.
        - Les informations fournies doivent être valides (type, format, contenu cohérents).

        POST:
        - Retourne True si les informations de profil ont été mises à jour.
        - Retourne False si la mise à jour échoue.

        RAISES:
        - ValueError: Si les nouvelles informations sont invalides.
        - PermissionError: Si l'utilisateur n'a pas les droits pour modifier son profil.
        """
        pass


class Notification:
    def envoyer(self):
        """
        Envoie une notification à un utilisateur donné.

        PRE:
        - Le destinataire doit être valide et identifiable.
        - Le contenu de la notification doit être fourni et valide.

        POST:
        - Retourne True si la notification est envoyée avec succès.
        - Retourne False si l'envoi échoue.

        RAISES:
        - ValueError: Si le destinataire ou le contenu est invalide.
        - NotificationError: Si une erreur technique survient pendant l’envoi.
        """
        pass

    def planifier(self):
        """
        Définit un horaire pour l’envoi d’une notification.

        PRE:
        - Une date et une heure valides doivent être spécifiées.
        - La date ne peut pas être dans le passé.

        POST:
        - Retourne True si la notification est correctement planifiée.
        - Retourne False si la planification échoue.

        RAISES:
        - ValueError: Si la date est invalide ou dans le passé.
        - NotificationError: Si une erreur survient lors de la planification.
        """
        pass


class Recompense:
    def verifier_condition(self):
        """
        Analyse si l’utilisateur répond aux critères de déblocage d’une récompense.

        PRE:
        - Les informations utilisateur nécessaires (ex. historique, scores) doivent être disponibles.

        POST:
        - Retourne True si les critères sont remplis.
        - Retourne False si les critères ne sont pas remplis.

        RAISES:
        - ValueError: Si les informations utilisateur sont manquantes ou invalides.
        """
        pass

    def debloquer(self):
        """
        Attribue une récompense si les critères de déblocage sont remplis.

        PRE:
        - Les critères de déblocage doivent être vérifiés et remplis.
        - Une connexion à la base de données doit être disponible.

        POST:
        - Retourne True si la récompense est attribuée avec succès.
        - Retourne False si l’attribution échoue.

        RAISES:
        - PermissionError: Si les critères ne sont pas remplis.
        - DatabaseError: Si une erreur survient lors de la mise à jour en base.
        """
        pass
