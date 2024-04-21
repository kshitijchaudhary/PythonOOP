from question import Question

class Quiz:
    def __init__(self, qList=[]):
        self._questions = qList

    def addQuestion(self, question):
        # Add a question to the quiz after validation
        if not isinstance(question, Question):
            print("Error: You may only add instances of the Question class")
        else:
            self._questions.append(question)

    def __add__(self, quiz02):
        # Combine two quizzes
        return Quiz(self._questions + quiz02._questions)

    def __len__(self):
        # Get the number of questions in the quiz
        return len(self._questions)

    def getTotalPoints(self):
        # Get the total points for the quiz
        return sum(q.getPoints() for q in self._questions)

    def __iter__(self):
        # Initialize the iterator
        self._index = 0
        return self

    def __next__(self):
        # Get the next question in the iterator
        if self._index < len(self._questions):
            result = self._questions[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration