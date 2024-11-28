import tkinter as tk
from tkinter import ttk, messagebox

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Application de Flashcards")

        # Configuration de la fenêtre principale
        self.root.geometry("800x600")

        # Menu principal
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Sous-menus
        self.user_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Utilisateur", menu=self.user_menu)
        self.user_menu.add_command(label="Ajouter un utilisateur", command=self.ajouter_utilisateur)
        self.user_menu.add_command(label="Sélectionner un utilisateur", command=self.selectionner_utilisateur)

        self.flashcard_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Flashcards", menu=self.flashcard_menu)
        self.flashcard_menu.add_command(label="Créer un set de flashcards", command=self.creer_set_flashcards)
        self.flashcard_menu.add_command(label="Réviser un set", command=self.reviser_set_flashcards)

        self.stats_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Statistiques", menu=self.stats_menu)
        self.stats_menu.add_command(label="Voir les statistiques", command=self.afficher_statistiques)

        # Section principale (contenu dynamique)
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Label par défaut
        self.default_label = ttk.Label(self.main_frame, text="Bienvenue dans l'application de Flashcards !",
                                       font=("Helvetica", 16))
        self.default_label.pack(pady=20)

    def ajouter_utilisateur(self):
        """Fenêtre pour ajouter un utilisateur."""
        def ajouter_action():
            nom = nom_entry.get().strip()
            email = email_entry.get().strip()
            if nom and email:
                # Simulation de l'ajout d'utilisateur
                messagebox.showinfo("Succès", f"Utilisateur '{nom}' ajouté avec succès !")
                ajout_utilisateur_window.destroy()
            else:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

        ajout_utilisateur_window = tk.Toplevel(self.root)
        ajout_utilisateur_window.title("Ajouter un utilisateur")
        ajout_utilisateur_window.geometry("400x300")

        tk.Label(ajout_utilisateur_window, text="Nom:").pack(pady=10)
        nom_entry = tk.Entry(ajout_utilisateur_window)
        nom_entry.pack(pady=10)

        tk.Label(ajout_utilisateur_window, text="Email:").pack(pady=10)
        email_entry = tk.Entry(ajout_utilisateur_window)
        email_entry.pack(pady=10)

        tk.Button(ajout_utilisateur_window, text="Ajouter", command=ajouter_action).pack(pady=20)

    def selectionner_utilisateur(self):
        """Fenêtre pour sélectionner un utilisateur."""
        messagebox.showinfo("Info", "Cette fonctionnalité sera implémentée prochainement.")

    def creer_set_flashcards(self):
        """Fenêtre pour créer un set de flashcards."""
        messagebox.showinfo("Info", "Cette fonctionnalité sera implémentée prochainement.")

    def reviser_set_flashcards(self):
        """Fenêtre pour réviser un set de flashcards."""
        messagebox.showinfo("Info", "Cette fonctionnalité sera implémentée prochainement.")

    def afficher_statistiques(self):
        """Fenêtre pour afficher les statistiques."""
        messagebox.showinfo("Info", "Cette fonctionnalité sera implémentée prochainement.")

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

