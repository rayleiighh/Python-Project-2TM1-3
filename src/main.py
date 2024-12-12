import datetime
from flashcard import Flashcard
from set_de_flashcard import SetDeFlashcards
from session_de_revision import SessionDeRevision
from utilisateur import Utilisateur
from statistiques import Statistiques
from statistiques_manager import StatistiquesManager
from notification import Notification
from recompense import Recompense

# Main Application

def main():
    utilisateurs = {}
    sets_de_flashcards = {}
    stats_manager = StatistiquesManager()

    while True:
        print("\nOptions principales :")
        print("1. Gestion des utilisateurs")
        print("2. Gestion des flashcards")
        print("3. Sessions de révision")
        print("4. Notifications")
        print("5. Statistiques")
        print("6. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            print("\nGestion des utilisateurs :")
            print("1. Ajouter un utilisateur")
            print("2. Se connecter")
            print("3. Se déconnecter")
            choix_utilisateur = input("Choisissez une option : ")

            if choix_utilisateur == "1":
                nom = input("Nom : ")
                email = input("Email : ")
                mot_de_passe = input("Mot de passe : ")
                try:
                    utilisateur = Utilisateur(nom, email, mot_de_passe)
                    utilisateurs[email] = utilisateur
                    stats_manager.update_statistiques(Statistiques(utilisateur_id=email, bonnes_reponses=0, cartes_revisees=0))
                    print("Utilisateur ajouté avec succès !")
                except ValueError as e:
                    print(f"Erreur : {e}")

            elif choix_utilisateur == "2":
                email = input("Email : ")
                mot_de_passe = input("Mot de passe : ")
                if email in utilisateurs and utilisateurs[email].se_connecter(email, mot_de_passe):
                    print("Connexion réussie !")
                else:
                    print("Échec de connexion.")

            elif choix_utilisateur == "3":
                email = input("Email : ")
                if email in utilisateurs and utilisateurs[email].se_deconnecter():
                    print("Déconnexion réussie !")
                else:
                    print("Aucune session active pour cet utilisateur.")

        elif choix == "2":
            print("\nGestion des flashcards :")
            print("1. Créer un set de flashcards")
            print("2. Ajouter une flashcard à un set")
            print("3. Modifier une flashcard")
            print("4. Supprimer une flashcard")
            choix_flashcard = input("Choisissez une option : ")

            if choix_flashcard == "1":
                email = input("Entrez votre email : ")
                if email in utilisateurs:
                    set_nom = input("Nom du set : ")
                    sets_de_flashcards[set_nom] = SetDeFlashcards(set_nom)
                    print(f"Set '{set_nom}' créé avec succès.")
                else:
                    print("Utilisateur introuvable.")

            elif choix_flashcard == "2":
                set_nom = input("Nom du set : ")
                if set_nom in sets_de_flashcards:
                    question = input("Question : ")
                    reponse = input("Réponse : ")
                    try:
                        flashcard = Flashcard(question, reponse)
                        sets_de_flashcards[set_nom].ajouter_flashcard(flashcard)
                        print("Flashcard ajoutée avec succès.")
                    except ValueError as e:
                        print(f"Erreur : {e}")
                else:
                    print("Set introuvable.")

            elif choix_flashcard == "3":
                set_nom = input("Nom du set : ")
                if set_nom in sets_de_flashcards:
                    ancienne_question = input("Question actuelle : ")
                    nouvelle_question = input("Nouvelle question : ")
                    nouvelle_reponse = input("Nouvelle réponse : ")
                    try:
                        sets_de_flashcards[set_nom].modifier_flashcard(ancienne_question, nouvelle_question, nouvelle_reponse)
                        print("Flashcard modifiée avec succès.")
                    except LookupError as e:
                        print(f"Erreur : {e}")
                else:
                    print("Set introuvable.")

            elif choix_flashcard == "4":
                set_nom = input("Nom du set : ")
                if set_nom in sets_de_flashcards:
                    question = input("Question de la flashcard à supprimer : ")
                    try:
                        sets_de_flashcards[set_nom].supprimer_flashcard(question)
                        print("Flashcard supprimée avec succès.")
                    except LookupError as e:
                        print(f"Erreur : {e}")
                else:
                    print("Set introuvable.")

        elif choix == "3":
            email = input("Email de l'utilisateur : ")
            if email in utilisateurs:
                set_nom = input("Nom du set à réviser : ")
                if set_nom in sets_de_flashcards:
                    session = SessionDeRevision(sets_de_flashcards[set_nom])
                    session.demarrer_session()
                    for flashcard in sets_de_flashcards[set_nom].flashcards:
                        print(f"Question : {flashcard.question}")
                        reponse = input("Votre réponse : ")
                        session.repondre_a_flashcard(flashcard, reponse)
                    session.terminer_session(stats_manager, email)
                    stats = session.afficher_statistiques()
                    print("Session terminée ! Voici vos statistiques :")
                    print(f"Cartes révisées : {stats['cartes_revisees']}")
                    print(f"Bonnes réponses : {stats['bonnes_reponses']}")
                    print(f"Pourcentage de réussite : {stats['pourcentage_reussite']:.2f}%")
                else:
                    print("Set introuvable.")
            else:
                print("Utilisateur introuvable.")

        elif choix == "5":
            email = input("Entrez votre email : ")
            try:
                stats = stats_manager.get_statistiques(email)
                print("Statistiques :")
                print(f"Email de l'utilisateur : {email}")
                print(f"Bonnes réponses : {stats.bonnes_reponses}")
                print(f"Cartes révisées : {stats.cartes_revisees}")
                print(f"Taux de rétention : {stats.calculer_taux_retention():.2f}%")
            except ValueError as e:
                print(f"Erreur : {e}")

        elif choix == "6":
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()
