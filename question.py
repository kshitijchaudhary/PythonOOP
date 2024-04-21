from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, qText, p):
        # Validate the question text and points
        if qText == "" or qText is None:
            print("Error: Empty question text provided. Aborting creation of Question.")
            exit()
        if p < 1:
            print("Error: Invalid points awarded to question. Aborting creation of Question.")
            exit()
        self._questionText = qText
        self._points = p

    @abstractmethod
    def getScore(self, answer):
        # Abstract method to be implemented by subclasses
        pass

    def __str__(self):
        # Return the question text
        return self._questionText

    def setQuestion(self, qText):
        # Set the question text after validation
        if qText == "" or qText is None:
            print("Error: Empty question text provided.")
        else:
            self._questionText = qText

    def getQuestion(self):
        # Get the question text
        return self._questionText

    def setPoints(self, p):
        # Set the points after validation
        if p < 1:
            print("Error: Invalid points awarded to question.")
        else:
            self._points = p

    def getPoints(self):
        # Get the points
        return self._points