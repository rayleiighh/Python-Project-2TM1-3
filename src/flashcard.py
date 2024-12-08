class Flashcard:
    def __init__(self, question, reponse):
        self.question = question
        self.reponse = reponse
        self.correct_count = 0
        self.incorrect_count = 0

    def repondre(self, reponse_utilisateur):
        if reponse_utilisateur.lower() == self.reponse.lower():
            self.correct_count += 1
            print("Bonne réponse !")
            return True
        else:
            self.incorrect_count += 1
            print(f"Mauvaise réponse. La bonne réponse est: {self.reponse}")
            return False

    def __str__(self):
        return f"Flashcard: {self.question}"
