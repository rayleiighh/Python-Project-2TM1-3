# Incrémenter par Mohamed Mokhtar El Mazani
class Recompense:
    def __init__(self, id, nom, description, condition_deblocage, utilisateur):
        self.id = id
        self.nom = nom
        self.description = description
        self.condition_deblocage = condition_deblocage
        self.utilisateur = utilisateur
        self.debloquee = False

    def verifier_condition(self, historique=None):
        """
        Vérifie si l'utilisateur remplit les critères pour débloquer la récompense.
        """
        if historique and self.condition_deblocage in historique:
            return True
        return False

    def debloquer(self, historique=None):
        """
        Débloque la récompense si les critères sont remplis.
        """
        if self.verifier_condition(historique):
            self.debloquee = True
            return True
        raise PermissionError("Critères non remplis pour débloquer la récompense")

    def __str__(self):
        return f"Recompense(id={self.id}, nom={self.nom}, debloquee={self.debloquee})"

