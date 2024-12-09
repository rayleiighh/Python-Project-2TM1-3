# Incrémenter par Mohamed Mokhtar El Mazani
import re

class Utilisateur:
    def __init__(self, nom, email, mot_de_passe):
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise ValueError("Email invalide")
        if len(mot_de_passe) < 8:
            raise ValueError("Le mot de passe doit contenir au moins 8 caractères")
        
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.session_active = False

    def __str__(self):
        return f"Utilisateur(nom={self.nom}, email={self.email}, session_active={self.session_active})"

    def se_connecter(self, email, mot_de_passe):
        if email == self.email and mot_de_passe == self.mot_de_passe:
            self.session_active = True
            return True
        return False

    def se_deconnecter(self):
        if self.session_active:
            self.session_active = False
            print("Déconnexion réussie.")
            return True
        print("Aucune session active.")
        return False

    def mettre_a_jour_profil(self):
        if not self.session_active:
            print("Vous devez être connecté pour mettre à jour votre profil.")
            return False
        nouveau_nom = input("Entrez un nouveau nom (laisser vide pour ne pas changer) : ")
        nouveau_email = input("Entrez un nouvel email (laisser vide pour ne pas changer) : ")
        nouveau_mot_de_passe = input("Entrez un nouveau mot de passe (laisser vide pour ne pas changer) : ")

        if nouveau_nom:
            self.nom = nouveau_nom
        if nouveau_email:
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", nouveau_email):
                print("Email invalide. Modification annulée.")
                return False
            self.email = nouveau_email
        if nouveau_mot_de_passe:
            if len(nouveau_mot_de_passe) < 8:
                print("Le mot de passe doit contenir au moins 8 caractères. Modification annulée.")
                return False
            self.mot_de_passe = nouveau_mot_de_passe
        print("Profil mis à jour avec succès.")
        return True
