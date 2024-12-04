import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class FlashcardApp:
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        self.utilisateur_actif = None  # L'utilisateur actif


        self.root.title("Application de Flashcards")
        self.root.geometry("800x600")
        self.charger_icones()
        # Menu principal
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Sous-menus
        self.user_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Utilisateur", menu=self.user_menu)
        self.user_menu.add_command(
            label="Ajouter un utilisateur",
            image=self.icone_ajouter_utilisateur,
            compound=tk.LEFT,  # Affiche l'image à gauche du texte
            command=self.ajouter_utilisateur
        )

        self.flashcard_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Flashcards", menu=self.flashcard_menu)
        self.flashcard_menu.add_command(
            label="Créer un set de flashcards",
            image=self.icone_creer_set,
            compound=tk.LEFT,
            command=self.creer_set_flashcards
        )
        self.flashcard_menu.add_command(
            label="Ajouter une flashcard",
            image=self.icone_ajouter_flashcard,
            compound=tk.LEFT,
            command=self.ajouter_flashcard
        )
        self.flashcard_menu.add_command(
            label="Réviser un set",
            image=self.icone_reviser_set,
            compound=tk.LEFT,
            command=self.reviser_set_flashcards
        )

        self.stats_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Statistiques", menu=self.stats_menu)
        self.stats_menu.add_command(label="Voir les statistiques", command=self.afficher_statistiques)

        # Section principale
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.default_label = ttk.Label(self.main_frame, text="Bienvenue dans l'application de Flashcards !",
                                       font=("Helvetica", 16))
        self.default_label.pack(pady=20)
        self.flashcard_menu.add_command(label="Gérer les Flashcards", command=self.choisir_set_pour_gerer_flashcards)
        self.flashcard_menu.add_command(label="Vérifier les Notifications", command=self.verifier_notifications)
        self.user_menu.add_command(
            label="Sélectionner un utilisateur",
            image=self.icone_selectionner_utilisateur,
            compound=tk.LEFT,
            command=self.selectionner_utilisateur
        )
        self.appliquer_style()

    from PIL import Image, ImageTk

    def charger_icones(self):
        """Charge et redimensionne les icônes pour les menus et boutons."""
        self.icone_ajouter_utilisateur = ImageTk.PhotoImage(
            Image.open("images/ajouter_utilisateur.png").resize((24, 24))
        )
        self.icone_selectionner_utilisateur = ImageTk.PhotoImage(
            Image.open("images/selectionner_utilisateur.png").resize((24, 24))
        )
        self.icone_creer_set = ImageTk.PhotoImage(
            Image.open("images/creer_set.png").resize((24, 24))
        )
        self.icone_ajouter_flashcard = ImageTk.PhotoImage(
            Image.open("images/ajouter_flashcard.png").resize((24, 24))
        )
        self.icone_reviser_set = ImageTk.PhotoImage(
            Image.open("images/reviser_set.png").resize((24, 24))
        )

    def ajouter_utilisateur(self):
        """Fenêtre pour ajouter un utilisateur."""
        if not self.utilisateur_actif:
            messagebox.showerror("Erreur", "Veuillez d'abord sélectionner un utilisateur.")
            return

        def ajouter_action():
            nom = nom_entry.get().strip()
            email = email_entry.get().strip()
            mot_de_passe = mdp_entry.get().strip()
            if nom and email and mot_de_passe:
                try:
                    self.db_manager.ajouter_utilisateur(nom, email, mot_de_passe)
                    messagebox.showinfo("Succès", f"Utilisateur '{nom}' ajouté avec succès !")
                    ajout_utilisateur_window.destroy()
                except Exception as e:
                    messagebox.showerror("Erreur", f"Impossible d'ajouter l'utilisateur : {e}")
            else:
                messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")

        ajout_utilisateur_window = tk.Toplevel(self.root)
        ajout_utilisateur_window.title("Ajouter un utilisateur")
        ajout_utilisateur_window.geometry("400x300")

        tk.Label(ajout_utilisateur_window, text="Nom:").pack(pady=5)
        nom_entry = tk.Entry(ajout_utilisateur_window)
        nom_entry.pack(pady=5)

        tk.Label(ajout_utilisateur_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(ajout_utilisateur_window)
        email_entry.pack(pady=5)

        tk.Label(ajout_utilisateur_window, text="Mot de passe:").pack(pady=5)
        mdp_entry = tk.Entry(ajout_utilisateur_window, show="*")
        mdp_entry.pack(pady=5)

        ajouter_button = tk.Button(
            self.root,
            text="Ajouter Flashcard",
            image=self.icone_ajouter_flashcard,
            compound=tk.LEFT,
            command=self.ajouter_flashcard
        )
        ajouter_button.pack(pady=10)

    def creer_set_flashcards(self):
        if not self.utilisateur_actif:
            messagebox.showerror("Erreur", "Veuillez d'abord sélectionner un utilisateur.")
            return

        """Fenêtre pour créer un set de flashcards."""
        if not self.utilisateur_actif:
            messagebox.showerror("Erreur", "Veuillez d'abord sélectionner un utilisateur.")
            return

        def creer_action():
            nom_set = set_name_entry.get().strip()
            if nom_set:
                try:
                    self.db_manager.ajouter_set_flashcards(nom_set,
                                                           self.utilisateur_actif)  # Utilise l'utilisateur actif
                    messagebox.showinfo("Succès", f"Set '{nom_set}' créé avec succès !")
                    creer_set_window.destroy()
                except Exception as e:
                    messagebox.showerror("Erreur", f"Impossible de créer le set : {e}")
            else:
                messagebox.showerror("Erreur", "Le nom du set ne peut pas être vide.")

        creer_set_window = tk.Toplevel(self.root)
        creer_set_window.title("Créer un set de flashcards")
        creer_set_window.geometry("400x200")

        tk.Label(creer_set_window, text="Nom du set de flashcards:").pack(pady=10)
        set_name_entry = tk.Entry(creer_set_window)
        set_name_entry.pack(pady=10)

        tk.Button(creer_set_window, text="Créer", command=creer_action).pack(pady=20)

    def ajouter_flashcard(self):
        if not self.utilisateur_actif:
            messagebox.showerror("Erreur", "Veuillez d'abord sélectionner un utilisateur.")
            return

        """Fenêtre pour ajouter une flashcard à un set."""
        def ajouter_action():
            set_id = int(set_id_entry.get().strip())
            question = question_entry.get().strip()
            reponse = reponse_entry.get().strip()
            if set_id and question and reponse:
                try:
                    self.db_manager.ajouter_flashcard(question, reponse, set_id)
                    messagebox.showinfo("Succès", "Flashcard ajoutée avec succès !")
                    ajouter_flashcard_window.destroy()
                except Exception as e:
                    messagebox.showerror("Erreur", f"Impossible d'ajouter la flashcard : {e}")
            else:
                messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")

        ajouter_flashcard_window = tk.Toplevel(self.root)
        ajouter_flashcard_window.title("Ajouter une flashcard")
        ajouter_flashcard_window.geometry("400x300")

        tk.Label(ajouter_flashcard_window, text="ID du set:").pack(pady=5)
        set_id_entry = tk.Entry(ajouter_flashcard_window)
        set_id_entry.pack(pady=5)

        tk.Label(ajouter_flashcard_window, text="Question:").pack(pady=5)
        question_entry = tk.Entry(ajouter_flashcard_window)
        question_entry.pack(pady=5)

        tk.Label(ajouter_flashcard_window, text="Réponse:").pack(pady=5)
        reponse_entry = tk.Entry(ajouter_flashcard_window)
        reponse_entry.pack(pady=5)

        tk.Button(ajouter_flashcard_window, text="Ajouter", command=ajouter_action).pack(pady=20)

    def reviser_set_flashcards(self):
        if not self.utilisateur_actif:
            messagebox.showerror("Erreur", "Veuillez d'abord sélectionner un utilisateur.")
            return

        """Fenêtre pour sélectionner un set et démarrer une révision."""

        def commencer_revision():
            selected_set = listbox.get(tk.ACTIVE)
            if selected_set:
                set_id = int(selected_set.split(":")[0])  # Extraire l'ID du set
                self.lancer_session_revision(set_id)
                revision_window.destroy()
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner un set.")

        revision_window = tk.Toplevel(self.root)
        revision_window.title("Réviser un set")
        revision_window.geometry("400x300")

        tk.Label(revision_window, text="Sélectionnez un set pour réviser:").pack(pady=10)
        listbox = tk.Listbox(revision_window)
        listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        utilisateur_id = 1  # En phase de test, utilisateur ID 1
        sets = self.db_manager.obtenir_sets_pour_utilisateur(utilisateur_id)
        for set_ in sets:
            listbox.insert(tk.END, f"{set_[0]}: {set_[1]}")  # ID et nom du set

        tk.Button(revision_window, text="Commencer", command=commencer_revision).pack(pady=20)

    def lancer_session_revision(self, set_id):
        """Démarre une session de révision pour un set spécifique."""
        flashcards = self.db_manager.obtenir_flashcards_pour_set(set_id)
        if not flashcards:
            messagebox.showinfo("Info", "Ce set ne contient pas de flashcards.")
            return
        self.db_manager.connection.execute("""
                UPDATE sets_de_flashcards
                SET dernier_revision = datetime('now')
                WHERE id = ?;
            """, (set_id,))

        session_window = tk.Toplevel(self.root)
        session_window.title("Session de Révision")
        session_window.geometry("400x300")

        current_index = [0]
        bonnes_reponses = [0]

        def afficher_question():
            if current_index[0] < len(flashcards):
                question_label.config(text=f"Question: {flashcards[current_index[0]][1]}")
                reponse_entry.delete(0, tk.END)
            else:
                terminer_session()

        def valider_reponse():
            user_reponse = reponse_entry.get().strip()
            correct_reponse = flashcards[current_index[0]][2]

            if user_reponse.lower() == correct_reponse.lower():
                bonnes_reponses[0] += 1
                self.db_manager.connection.execute(
                    "UPDATE flashcards SET correct_count = correct_count + 1 WHERE id = ?;",
                    (flashcards[current_index[0]][0],)
                )
            else:
                self.db_manager.connection.execute(
                    "UPDATE flashcards SET incorrect_count = incorrect_count + 1 WHERE id = ?;",
                    (flashcards[current_index[0]][0],)
                )
            current_index[0] += 1
            afficher_question()

        def terminer_session():
            session_window.destroy()
            messagebox.showinfo(
                "Session terminée",
                f"Session terminée ! Bonnes réponses: {bonnes_reponses[0]} / {len(flashcards)}"
            )

        question_label = tk.Label(session_window, text="", font=("Helvetica", 14))
        question_label.pack(pady=10)

        reponse_entry = tk.Entry(session_window)
        reponse_entry.pack(pady=10)

        tk.Button(session_window, text="Valider", command=valider_reponse).pack(pady=10)
        afficher_question()

    def afficher_statistiques(self):
        if not self.utilisateur_actif:
            messagebox.showerror("Erreur", "Veuillez d'abord sélectionner un utilisateur.")
            return

        """Fenêtre pour afficher les statistiques."""
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Statistiques")
        stats_window.geometry("600x400")

        # Section des statistiques globales
        tk.Label(stats_window, text="Statistiques Globales", font=("Helvetica", 14)).pack(pady=10)

        globales = self.db_manager.obtenir_statistiques_globales()
        tk.Label(stats_window, text=f"Total Correct: {globales['correct']}", font=("Helvetica", 12)).pack()
        tk.Label(stats_window, text=f"Total Incorrect: {globales['incorrect']}", font=("Helvetica", 12)).pack()
        tk.Label(stats_window, text=f"Taux de Réussite: {globales['taux_reussite']:.2f}%", font=("Helvetica", 12)).pack(
            pady=10)

        # Section des statistiques par set
        tk.Label(stats_window, text="Statistiques par Set", font=("Helvetica", 14)).pack(pady=10)

        stats_tree = ttk.Treeview(stats_window, columns=("Set", "Correct", "Incorrect", "Taux"), show="headings")
        stats_tree.heading("Set", text="Set")
        stats_tree.heading("Correct", text="Correct")
        stats_tree.heading("Incorrect", text="Incorrect")
        stats_tree.heading("Taux", text="Taux de Réussite (%)")
        stats_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        stats_par_set = self.db_manager.obtenir_statistiques_par_set()
        for set_stats in stats_par_set:
            stats_tree.insert("", tk.END, values=set_stats)

    def gerer_flashcards(self, set_id):
        """Fenêtre pour gérer les flashcards d’un set."""
        gestion_window = tk.Toplevel(self.root)
        gestion_window.title("Gérer les Flashcards")
        gestion_window.geometry("600x400")

        tk.Label(gestion_window, text="Flashcards du Set", font=("Helvetica", 14)).pack(pady=10)

        # Tableau des flashcards
        flashcards_tree = ttk.Treeview(gestion_window, columns=("ID", "Question", "Réponse"), show="headings")
        flashcards_tree.heading("ID", text="ID")
        flashcards_tree.heading("Question", text="Question")
        flashcards_tree.heading("Réponse", text="Réponse")
        flashcards_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Charger les flashcards
        flashcards = self.db_manager.obtenir_flashcards_pour_set(set_id)
        for flashcard in flashcards:
            flashcards_tree.insert("", tk.END, values=flashcard)

        # Boutons Modifier et Supprimer
        def modifier_flashcard():
            selected_item = flashcards_tree.selection()
            if selected_item:
                flashcard_id = flashcards_tree.item(selected_item, "values")[0]
                self.modifier_flashcard(int(flashcard_id))
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner une flashcard.")

        def supprimer_flashcard():
            selected_item = flashcards_tree.selection()
            if selected_item:
                flashcard_id = flashcards_tree.item(selected_item, "values")[0]
                self.db_manager.supprimer_flashcard(int(flashcard_id))
                flashcards_tree.delete(selected_item)
                messagebox.showinfo("Succès", "Flashcard supprimée avec succès.")
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner une flashcard.")

        tk.Button(gestion_window, text="Modifier", command=modifier_flashcard).pack(side=tk.LEFT, padx=20, pady=10)
        tk.Button(gestion_window, text="Supprimer", command=supprimer_flashcard).pack(side=tk.RIGHT, padx=20, pady=10)

    def modifier_flashcard(self, flashcard_id):
        """Fenêtre pour modifier une flashcard."""
        modifier_window = tk.Toplevel(self.root)
        modifier_window.title("Modifier une Flashcard")
        modifier_window.geometry("400x300")

        tk.Label(modifier_window, text="Nouvelle Question:").pack(pady=5)
        question_entry = tk.Entry(modifier_window)
        question_entry.pack(pady=5)

        tk.Label(modifier_window, text="Nouvelle Réponse:").pack(pady=5)
        reponse_entry = tk.Entry(modifier_window)
        reponse_entry.pack(pady=5)

        def enregistrer_modifications():
            nouvelle_question = question_entry.get().strip()
            nouvelle_reponse = reponse_entry.get().strip()
            if nouvelle_question and nouvelle_reponse:
                self.db_manager.modifier_flashcard(flashcard_id, nouvelle_question, nouvelle_reponse)
                messagebox.showinfo("Succès", "Flashcard modifiée avec succès.")
                modifier_window.destroy()
            else:
                messagebox.showerror("Erreur", "Les champs Question et Réponse ne peuvent pas être vides.")

        tk.Button(modifier_window, text="Enregistrer", command=enregistrer_modifications).pack(pady=20)

    def choisir_set_pour_gerer_flashcards(self):
        """Fenêtre pour choisir un set et gérer ses flashcards."""
        if not self.utilisateur_actif:
            messagebox.showerror("Erreur", "Veuillez d'abord sélectionner un utilisateur.")
            return

        choisir_window = tk.Toplevel(self.root)
        choisir_window.title("Choisir un Set")
        choisir_window.geometry("400x300")

        tk.Label(choisir_window, text="Sélectionnez un set pour gérer ses flashcards:", font=("Helvetica", 12)).pack(
            pady=10)

        listbox = tk.Listbox(choisir_window)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Charger les sets depuis la base de données
        sets = self.db_manager.obtenir_sets_pour_utilisateur(self.utilisateur_actif)
        for set_ in sets:
            listbox.insert(tk.END, f"{set_[0]}: {set_[1]}")  # ID et nom du set

        def ouvrir_gestion_flashcards():
            selected_item = listbox.get(tk.ACTIVE)
            if selected_item:
                set_id = int(selected_item.split(":")[0])  # Extraire l'ID du set
                self.gerer_flashcards(set_id)
                choisir_window.destroy()
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner un set.")

        tk.Button(choisir_window, text="Ouvrir", command=ouvrir_gestion_flashcards).pack(pady=20)

    def verifier_notifications(self):
        if not self.utilisateur_actif:
            messagebox.showerror("Erreur", "Veuillez d'abord sélectionner un utilisateur.")
            return

        """Vérifie les sets à réviser et affiche une notification."""
        sets_a_reviser = self.db_manager.obtenir_sets_a_reviser()
        if sets_a_reviser:
            noms_sets = "\n".join([f"{set_[1]} (Dernière révision : {set_[2] or 'Jamais'})" for set_ in sets_a_reviser])
            messagebox.showinfo(
                "Rappel de Révision",
                f"Vous avez des sets à réviser :\n\n{noms_sets}"
            )
        else:
            messagebox.showinfo("Rappel de Révision", "Tous les sets sont à jour !")

    def selectionner_utilisateur(self):
        """Fenêtre pour sélectionner un utilisateur."""
        selection_window = tk.Toplevel(self.root)
        selection_window.title("Sélectionner un Utilisateur")
        selection_window.geometry("400x300")

        tk.Label(selection_window, text="Sélectionnez un utilisateur :", font=("Helvetica", 12)).pack(pady=10)

        listbox = tk.Listbox(selection_window)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Charger les utilisateurs depuis la base de données
        utilisateurs = self.db_manager.obtenir_utilisateurs()
        for utilisateur in utilisateurs:
            listbox.insert(tk.END, f"{utilisateur[0]}: {utilisateur[1]}")  # ID et Nom

        def confirmer_selection():
            selected_item = listbox.get(tk.ACTIVE)
            if selected_item:
                utilisateur_id = int(selected_item.split(":")[0])  # Extraire l'ID de l'utilisateur
                self.utilisateur_actif = utilisateur_id
                utilisateur_nom = selected_item.split(":")[1].strip()
                messagebox.showinfo("Succès", f"Utilisateur sélectionné : {utilisateur_nom}")
                selection_window.destroy()
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner un utilisateur.")

        tk.Button(selection_window, text="Confirmer", command=confirmer_selection).pack(pady=20)

    def appliquer_style(self):
        """Applique un thème moderne aux widgets."""
        style = ttk.Style()
        style.theme_use("clam")  # Utilise un thème moderne (clam, alt, default, classic)

        # Style des boutons
        style.configure("TButton", font=("Helvetica", 12), padding=5, background="#5D9CEC", foreground="white")
        style.map("TButton", background=[("active", "#4A8BCD")])

        # Style des labels
        style.configure("TLabel", font=("Helvetica", 12), padding=5)

        # Style des menus
        self.root.config(background="#F4F4F4")


# Lancer l'application
if __name__ == "__main__":
    from db_manager import DatabaseManager

    db_manager = DatabaseManager()  # Charger la base de données
    db_manager.create_tables()  # Crée les tables si elles n'existent pas
    db_manager.ajouter_colonne_dernier_revision()  # Ajoute la colonne 'dernier_revision'
    root = tk.Tk()
    app = FlashcardApp(root, db_manager)
    root.mainloop()
