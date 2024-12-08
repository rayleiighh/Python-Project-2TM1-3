from db_manager import DatabaseManager

db = DatabaseManager()

def afficher_menu():
    print("\n=== Menu Principal ===")
    print("1. Ajouter un utilisateur")
    print("2. Créer un set de flashcards")
    print("3. Ajouter une flashcard à un set")
    print("4. Réviser un set")
    print("5. Afficher les utilisateurs et leurs sets")
    print("6. Quitter")

def choisir_utilisateur():
    utilisateurs = db.obtenir_utilisateurs()
    if not utilisateurs:
        print("Aucun utilisateur. Veuillez en ajouter un.")
        return None
    for i, utilisateur in enumerate(utilisateurs, start=1):
        print(f"{i}. {utilisateur[1]} ({utilisateur[2]})")
    choix = int(input("Choisissez un utilisateur : ")) - 1
    return utilisateurs[choix]

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            nom = input("Nom : ")
            email = input("Email : ")
            db.ajouter_utilisateur(nom, email)
            print(f"Utilisateur {nom} ajouté.")

        elif choix == "2":
            utilisateur = choisir_utilisateur()
            if utilisateur:
                nom_set = input("Nom du set : ")
                db.ajouter_set(nom_set, utilisateur[0])
                print(f"Set {nom_set} ajouté pour {utilisateur[1]}.")

        elif choix == "3":
            utilisateur = choisir_utilisateur()
            if utilisateur:
                sets = db.obtenir_sets(utilisateur[0])
                for i, set_ in enumerate(sets, start=1):
                    print(f"{i}. {set_[1]}")
                set_index = int(input("Choisissez un set : ")) - 1
                set_id = sets[set_index][0]
                question = input("Question : ")
                reponse = input("Réponse : ")
                db.ajouter_flashcard(question, reponse, set_id)
                print("Flashcard ajoutée.")

        elif choix == "4":
            utilisateur = choisir_utilisateur()
            if utilisateur:
                sets = db.obtenir_sets(utilisateur[0])
                for i, set_ in enumerate(sets, start=1):
                    print(f"{i}. {set_[1]}")
                set_index = int(input("Choisissez un set : ")) - 1
                set_id = sets[set_index][0]
                flashcards = db.obtenir_flashcards(set_id)
                for flashcard in flashcards:
                    print(f"Question : {flashcard[1]}")
                    reponse_utilisateur = input("Votre réponse : ")
                    if reponse_utilisateur.lower() == flashcard[2].lower():
                        print("Bonne réponse !")
                    else:
                        print(f"Mauvaise réponse. La bonne réponse est : {flashcard[2]}")

        elif choix == "5":
            utilisateurs = db.obtenir_utilisateurs()
            for utilisateur in utilisateurs:
                print(f"Utilisateur : {utilisateur[1]}")
                sets = db.obtenir_sets(utilisateur[0])
                for set_ in sets:
                    print(f"  - {set_[1]}")

        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    main()
