# Incrémenter par Mohamed Mokhtar El Mazani


import datetime

class Utilisateur:
    def __init__(self, nom, email, mot_de_passe):
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.parametres = {}
        self.session_active = False

    def se_connecter(self, email, mot_de_passe):
        """
        Simule l'authentification de l'utilisateur.
        """
        if email == self.email and mot_de_passe == self.mot_de_passe:
            self.session_active = True
            return True
        raise ValueError("Informations d'authentification invalides")

    def se_deconnecter(self):
        """
        Met fin à la session utilisateur.
        """
        if self.session_active:
            self.session_active = False
            return True
        raise RuntimeError("Aucune session active")

    def mettre_a_jour_profil(self, nouveau_nom=None, nouveau_email=None, nouveau_mot_de_passe=None):
        """
        Met à jour les informations du profil utilisateur.
        """
        if not self.session_active:
            raise PermissionError("Utilisateur non connecté")
        if nouveau_nom:
            self.nom = nouveau_nom
        if nouveau_email:
            self.email = nouveau_email
        if nouveau_mot_de_passe:
            self.mot_de_passe = nouveau_mot_de_passe
        return True



