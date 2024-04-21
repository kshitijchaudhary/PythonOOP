from question import Question
from choice import Choice


class MultipleChoice(Question):
    def __init__(self, qText, choiceText, p, answer):
        # Call the parent class constructor
        super().__init__(qText, p)
        if len(choiceText) != 4:
            print("Error: Invalid number of choices provided for Multiple Choice question.")
            exit()
        self._choices = choiceText
        self._correctAnswer = answer

    def getScore(self, answer):
        # Calculate the score based on the user's answer
        if answer is None or len(answer) == 0:
            return 0
        answer = answer[0].strip().upper()
        if len(answer) > 1:
            answer = answer[0]
        return self._points if Choice[answer].value == self._correctAnswer.value else 0

    def __str__(self):
        # Return the question in the desired format
        choices = "\n".join([f"{choice.name}. {self._choices[choice.value - 1]}" for choice in Choice])
        return f"Multiple Choice:\nPoints: {self._points}\n{self._questionText}\n{choices}"

    def setCorrectAnswer(self, answer):
        # Set the correct answer after validation
        if answer in ["A", "B", "C", "D"]:
            self._correctAnswer = Choice[answer]
        else:
            print("Error: Invalid choice provided for Multiple Choice question.")

    def getCorrectAnswer(self):
        # Get the correct answer
        return self._correctAnswer.name