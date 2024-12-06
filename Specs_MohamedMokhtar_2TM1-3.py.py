class Utilisateur:
    
    def se_connecter(self):
        """
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA CACA
        Authentifie l'utilisateur avec les informations fournies.

        Cette méthode vérifie les informations d'identification de l'utilisateur 
        (par exemple, nom et mot de passe) et établit une session de connexion si 
        les informations sont valides.

        :param: Aucun paramètre 
        
        :return: 
            bool: True si la connexion est réussie, False sinon.

        :except:    
            ValueError: Si les informations d'identification sont manquantes.
            ConnectionError: Si une erreur de connexion au serveur survient.
        
        """
        pass

    
    def se_deconnecter(self):
        """
        Termine la session de l'utilisateur.
        Cette méthode met fin à la session de l'utilisateur en supprimant les 
        informations de session et en actualisant l'état de connexion.

        :param: Aucun paramètre 

        :return:
            bool: True si la déconnexion est réussie, False sinon.
            

        :except:    
            RuntimeError: Si l'utilisateur n'est pas connecté.
        
        """
        pass


    def  mettre_a_jour_profil(self):
        """
        Met à jour les informations du profil de l'utilisateur.

        Permet à l'utilisateur de modifier certaines informations de profil 
        (comme sa photo de profil, son nom, son email,son mot de passe et etc) et de sauvegarder les modifications.

        :param: Aucun paramètre 

        
        :return: 
            bool: True si la mise à jour a réussi, False sinon.
        
        :except:    
            ValueError: Si les informations fournies ne sont pas valides.
            PermissionError: Si l'utilisateur n'a pas les droits pour effectuer la mise à jour.
        
        """

        pass



class Notification:
    
    def envoyer(self):
        """
        Envoie une notification à l'utilisateur.

        Cette méthode envoie la notification spécifiée à l'utilisateur.

        :param: Aucun paramètre 

        Args:
            destinataire (Utilisateur): L'utilisateur qui recevra la notification.
            contenu (str): Le contenu de la notification.
            date_envoi (datetime): La date et heure à laquelle la notification doit être envoyée.

        :return: 
            bool: True si la notification a été envoyée avec succès, False sinon.

        :except:    
            ValueError: Si le destinataire ou le contenu de la notification est invalide.
            NotificationError: Si une erreur survient lors de l'envoi de la notification.
        
        """
        pass

    def planifier(self):
        """
        Planifie une notification pour être envoyée ultérieurement.

        Cette méthode permet de définir un horaire pour l'envoi d'une notification, par exemple 
        pour envoyer des rappels ou des messages à des heures précises.

        :param: Aucun paramètre 
 
        :return: 
            bool: True si la notification a été planifiée avec succès, False sinon.

        :except:    
            ValueError: Si la date d'envoi est dans le passé ou si les informations sont invalides.
            NotificationError: Si une erreur survient lors de la planification de la notification.
        
        """
        pass


class Recompense:
    def verifier_condition(self):
        """
        Vérifie si l'utilisateur remplit les conditions pour débloquer une récompense.

        Cette méthode analyse les critères de déblocage de la récompense (par exemple, nombre 
        de sessions de révision, taux de réussite, etc.) et vérifie si l'utilisateur 
        remplit à ces critères.

        :param: Aucun paramètre 

        :return: 
            bool: True si la condition est remplie, False sinon.

        :except:    
            ValueError: Si les informations de l'utilisateur sont invalides ou manquantes.
        
        """
        pass

    def debloquer(self):
        """
        Débloque la récompense pour l'utilisateur si les conditions sont remplies.

        Cette méthode attribue la récompense à l'utilisateur après vérification des conditions 
        et met à jour l'état de la récompense.

        :param: Aucun paramètre 

        :return: 
            bool: True si la récompense a été débloquée avec succès, False sinon.

        :except:    
            PermissionError: Si les conditions de déblocage ne sont pas remplies.
            DatabaseError: Si une erreur survient lors de la mise à jour en base de données.
        
        """
        pass

