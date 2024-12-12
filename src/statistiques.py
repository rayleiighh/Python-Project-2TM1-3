class Statistiques:
    def __init__(self, utilisateur_id: int, bonnes_reponses: int, cartes_revisees: int):
        self.utilisateur_id = utilisateur_id
        self.bonnes_reponses = bonnes_reponses
        self.cartes_revisees = cartes_revisees
    
    def calculer_taux_retention(self) -> float:
        """
        Calcule le taux de rétention basé sur les bonnes réponses et les cartes révisées.

        Retour:
        - Un float représentant le taux de rétention.
        
        Exception:
        ZeroDivisionError: Si le nombre total de cartes révisées est zéro, empêchant le calcul du taux de rétention.
        """
        if self.cartes_revisees == 0:
            raise ZeroDivisionError("Le nombre total de cartes révisées est zéro.")
        return (self.bonnes_reponses / self.cartes_revisees) * 100

    def afficher_graphique(self) -> None:
        """
        Affiche un graphique des statistiques de révision.

        
        Exception:
        - ValueError: Si les données nécessaires pour afficher le graphique sont manquantes ou invalides.
        """
        if self.cartes_revisees == 0:
            raise ValueError("Pas de données disponibles pour afficher le graphique.")
        
        # Représentation textuelle des statistiques
        bonnes_reponses_ratio = self.bonnes_reponses / self.cartes_revisees
        mauvaises_reponses_ratio = 1 - bonnes_reponses_ratio

        graphique = [
            f"Bonnes Réponses: {'#' * int(bonnes_reponses_ratio * 50)} {self.bonnes_reponses} ({bonnes_reponses_ratio:.1%})",
            f"Mauvaises Réponses: {'#' * int(mauvaises_reponses_ratio * 50)} {self.cartes_revisees - self.bonnes_reponses} ({mauvaises_reponses_ratio:.1%})"
        ]

        print("\n".join(graphique))

