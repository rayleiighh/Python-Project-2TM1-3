from utilisateur import Utilisateur

# Liste pour stocker les utilisateurs créés
utilisateurs = []

# Création d'un utilisateur
while True:
    try:
        nom = input("Entrez votre nom : ")
        email = input("Entrez votre email : ")
        mot_de_passe = input("Entrez un mot de passe (minimum 8 caractères) : ")
        utilisateur = Utilisateur(nom, email, mot_de_passe)
        utilisateurs.append(utilisateur)
        print(f"Utilisateur {nom} créé avec succès.")
        break
    except ValueError as e:
        print(f"Erreur : {e}")

# Connexion
while True:
    print("\nConnexion :")
    email_connexion = input("Entrez votre email : ")
    mot_de_passe_connexion = input("Entrez votre mot de passe : ")

    if utilisateur.se_connecter(email_connexion, mot_de_passe_connexion):
        print(f"Bienvenue, {utilisateur.nom} !")
        break
    else:
        print("Email ou mot de passe incorrect. Veuillez réessayer.")

# Menu principal
while utilisateur.session_active:
    print("\nMenu Principal :")
    print("1 - Se connecter avec un autre compte")
    print("2 - Se déconnecter")
    print("3 - Mettre à jour son profil")
    print("4 - Quitter")

    choix = input("Entrez votre choix : ")
    if choix == "1":
        utilisateur.se_deconnecter()
        while True:
            email_connexion = input("Entrez votre email : ")
            mot_de_passe_connexion = input("Entrez votre mot de passe : ")
            utilisateur = next(
                (u for u in utilisateurs if u.se_connecter(email_connexion, mot_de_passe_connexion)), None
            )
            if utilisateur:
                print(f"Bienvenue, {utilisateur.nom} !")
                break
            else:
                print("Email ou mot de passe incorrect. Veuillez réessayer.")
    elif choix == "2":
        utilisateur.se_deconnecter()
    elif choix == "3":
        utilisateur.mettre_a_jour_profil()
    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")

# Afficher les utilisateurs créés
print("\nListe des utilisateurs créés :")
for u in utilisateurs:
    print(u)
