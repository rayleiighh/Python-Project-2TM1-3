import datetime

class Notification:
    def __init__(self, id, type, contenu, utilisateur):
        self.id = id
        self.type = type
        self.contenu = contenu
        self.utilisateur = utilisateur

    def envoyer(self):
        """
        Simule l'envoi d'une notification.
        """
        if not self.contenu:
            raise ValueError("Le contenu de la notification est vide")
        print(f"Notification envoyée à {self.utilisateur.nom}: {self.contenu}")
        return True

    def planifier(self, date):
        """
        Planifie une notification à une date future.
        """
        if not isinstance(date, datetime.datetime) or date < datetime.datetime.now():
            raise ValueError("Date invalide pour la planification")
        print(f"Notification planifiée pour le {date.strftime('%Y-%m-%d %H:%M:%S')}")
        return True


