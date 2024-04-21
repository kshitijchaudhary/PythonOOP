from question import Question

class FillInBlank(Question):
    def __init__(self, qText, p, answer):
        # Call the parent class constructor and format the question text
        super().__init__(" ".join(qText[:-1]) + " ".join(["_______ "] * (len(qText) - 1)), p)
        self._numBlanks = len(qText) - 1
        if answer is None or len(answer) != self._numBlanks:
            print("Error: Invalid number of answers provided for Fill in the Blank question.")
            exit()
        self._correctAnswer = [ans.strip().lower() for ans in answer]

    def getScore(self, answer):
        # Calculate the score based on the user's answer
        if answer is None or len(answer) != self._numBlanks:
            return 0
        score = 0
        for i in range(self._numBlanks):
            if answer[i].strip().lower() == self._correctAnswer[i]:
                score += 1
        return self._points * (score / self._numBlanks)

    def __str__(self):
        # Return the question in the desired format
        return f"Fill in Blank:\nPoints: {self._points}\n{self._questionText}"

    def setCorrectAnswer(self, answer):
        # Set the correct answer after validation
        if len(answer) != self._numBlanks:
            print("Error: Invalid number of answers provided for Fill in the Blank question.")
        else:
            self._correctAnswer = [ans.strip().lower() for ans in answer]

    def getCorrectAnswer(self):
        # Get the correct answer
        return self._correctAnswer