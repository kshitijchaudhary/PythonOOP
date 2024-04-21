import random
from question import Question

class Matching(Question):
    def __init__(self, qText, questionsAndMatches, allOrNothing, p):
        # Call the parent class constructor
        super().__init__(qText, p)
        if len(questionsAndMatches) != 2 or len(questionsAndMatches[0]) != len(questionsAndMatches[1]):
            print("Error: Invalid format for Matching question.")
            exit()
        self._matchingQuestions = questionsAndMatches
        self._allOrNothing = allOrNothing

    def getScore(self, answer):
        # Calculate the score based on the user's answer
        if answer is None or len(answer) != len(self._matchingQuestions[0]):
            return 0
        score = 0
        for i in range(len(self._matchingQuestions[0])):
            if answer[i].strip().lower() == self._matchingQuestions[1][i].strip().lower():
                score += 1
        if self._allOrNothing and score == len(self._matchingQuestions[0]):
            return self._points
        else:
            return self._points * (score / len(self._matchingQuestions[0]))

    def __str__(self):
        # Return the question in the desired format
        options = ", ".join(random.sample(self._matchingQuestions[1], len(self._matchingQuestions[1])))
        questions = "\n".join([f"{i + 1}){self._matchingQuestions[0][i]}" for i in range(len(self._matchingQuestions[0]))])
        return f"Matching:\nPoints: {self._points}\nAll or Nothing: {self._allOrNothing}\n{self._questionText}\n{questions}\nOptions: {options}"