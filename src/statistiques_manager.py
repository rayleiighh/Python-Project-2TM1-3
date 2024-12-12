from statistiques import Statistiques

class DatabaseError(Exception):
    """Exception levée lorsqu'il y a une erreur liée à la base de données."""
    pass

class StatistiquesManager:
    def __init__(self):
        self._db = {}  # Base de données simulée

    def get_statistiques(self, utilisateur_id: int) -> Statistiques:
        """
        Récupère les statistiques d'un utilisateur spécifique.

        Paramètre :
        - utilisateur_id: l'identifiant unique de l'utilisateur.

        Retour : 
        - stats: un objet Statistiques contenant les statistiques de l'utilisateur.

        Exceptions :
        - ValueError: si l'utilisateur avec l'ID spécifié n'existe pas.
        - DatabaseError: Si une erreur survient lors de la réinitialisation des données dans la base de données.
        """
        if utilisateur_id not in self._db:
            raise ValueError(f"L'utilisateur avec l'ID {utilisateur_id} n'existe pas.")
        return self._db[utilisateur_id]

    def update_statistiques(self, statistiques: Statistiques) -> None:
        """
        Met à jour les statistiques pour un utilisateur.

        Paramètre:
        - statistiques: un objet Statistiques contenant les nouvelles valeurs à mettre à jour.

        Exceptions:
        - ValueError: si les statistiques fournies ne sont pas valides.
        - DatabaseError: Si une erreur survient lors de la réinitialisation des données dans la base de données.

        """
        if not isinstance(statistiques, Statistiques):
            raise ValueError("Les statistiques fournies ne sont pas valides.")
        self._db[statistiques.utilisateur_id] = statistiques

    def reset_statistiques(self, utilisateur_id: int) -> None:
        """
        Réinitialise les statistiques d'un utilisateur spécifique.

        Paramètre: 
        -utilisateur_id: L'identifiant unique de l'utilisateur.

        Exceptions:
        - ValueError: Si l'utilisateur avec l'ID spécifié n'existe pas.
        - DatabaseError: Si une erreur survient lors de la réinitialisation des données dans la base de données.
        """
        if utilisateur_id not in self._db:
            raise ValueError(f"L'utilisateur avec l'ID {utilisateur_id} n'existe pas.")
        try:
            self._db[utilisateur_id] = Statistiques(utilisateur_id, 0, 0)
        except Exception as e:
            raise DatabaseError("Erreur lors de la réinitialisation des données dans la base de données.") from e
