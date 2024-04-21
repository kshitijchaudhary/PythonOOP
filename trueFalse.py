from question import Question

class TrueFalse(Question):
    def __init__(self, qText, p, answer):
        # Call the parent class constructor
        super().__init__(qText, p)
        self._correctAnswer = answer

    def getScore(self, answer):
        # Calculate the score based on the user's answer
        if answer is None or len(answer) == 0:
            return 0
        answer = answer[0].lower() == "true" if self._correctAnswer else answer[0].lower() == "false"
        return self._points if answer else 0

    def __str__(self):
        # Return the question in the desired format
        return f"True or False:\nPoints: {self._points}\n{self._questionText}"

    def setCorrectAnswer(self, answer):
        # Set the correct answer
        self._correctAnswer = answer

    def getCorrectAnswer(self):
        # Get the correct answer
        return self._correctAnswer