from tkinter import messagebox

def require_active_user(func):
    """
    Décorateur pour vérifier qu'un utilisateur actif est sélectionné
    avant d'exécuter une méthode.
    """
    def wrapper(self, *args, **kwargs):
        if not self.utilisateur_actif:
            messagebox.showerror("Erreur", "Veuillez d'abord sélectionner un utilisateur.")
            return
        return func(self, *args, **kwargs)
    return wrapper
