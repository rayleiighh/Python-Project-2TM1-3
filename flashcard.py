class Flashcard:
    def __init__(self, question, reponse):
        self.question = question
        self.reponse = reponse
        self.correct_count = 0
        self.incorrect_count = 0

    def afficher_question(self):
        return f"Question: {self.question}"

    def verifier_reponse(self, reponse):
        if reponse.strip().lower() == self.reponse.lower():
            self.correct_count += 1
            return True
        else:
            self.incorrect_count += 1
            return False
