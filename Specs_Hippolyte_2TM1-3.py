class StatistiquesManager:
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

        pass

    def update_statistiques(self, statistiques: Statistiques) -> None:
        """
        Met à jour les statistiques pour un utilisateur.

        Paramètre:
        - statistiques: un objet Statistiques contenant les nouvelles valeurs à mettre à jour.

        Exceptions:
        - ValueError: si les statistiques fournies ne sont pas valides.
        - DatabaseError: Si une erreur survient lors de la réinitialisation des données dans la base de données.

        """

        pass

    def reset_statistiques(self, utilisateur_id: int) -> None:
        """
        Réinitialise les statistiques d'un utilisateur spécifique.

        Paramètre: 
        -utilisateur_id: L'identifiant unique de l'utilisateur.

        Exceptions:
        - ValueError: Si l'utilisateur avec l'ID spécifié n'existe pas.
        - DatabaseError: Si une erreur survient lors de la réinitialisation des données dans la base de données.
        """
        pass



class Statistiques:
    def calculer_taux_retention(self) -> float:
        """
        Calcule le taux de rétention basé sur les bonnes réponses et les cartes révisées.

        Retour:
        - Un float représentant le taux de rétention.
        
        Exception:
        ZeroDivisionError: Si le nombre total de cartes révisées est zéro, empêchant le calcul du taux de rétention.
        """
        pass

    def afficher_graphique(self) -> None:
        """
        Affiche un graphique des statistiques de révision.

        
        Exception:
        - ValueError: Si les données nécessaires pour afficher le graphique sont manquantes ou invalides.
        """
        pass