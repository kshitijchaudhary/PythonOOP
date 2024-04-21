import os
from question import Question
from fillInBlank import FillInBlank
from trueFalse import TrueFalse
from choice import Choice
from multipleChoice import MultipleChoice
from matching import Matching
from quiz import Quiz
import sys

def readQuiz(filename):
    questions = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    with open(file_path, "r") as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            try:
                qType = lines[i].strip()
                points_line = lines[i + 1].strip()
                if not points_line.startswith("Points:"):
                    raise ValueError(f"Invalid format in quiz.txt at line {i + 2}")
                points = int(points_line.split(":")[1])
                if qType == "True or False":
                    qText = lines[i + 2].strip('"')
                    answer = lines[i + 3].strip() == "True"
                    questions.append(TrueFalse(qText, points, answer))
                    i += 4
                elif qType == "Fill in Blank":
                    qText = lines[i + 2:i + 4]
                    answer = lines[i + 4].strip('"').split('", "')
                    questions.append(FillInBlank(qText, points, answer))
                    i += 5
                elif qType == "Multiple Choice":
                    qText = lines[i + 2].strip('"')
                    choices = [line.strip('"') for line in lines[i + 3:i + 7]]
                    answer = Choice[lines[i + 7].strip()]
                    questions.append(MultipleChoice(qText, choices, points, answer))
                    i += 8
                elif qType == "Matching":
                    qText = lines[i + 2].strip('"')
                    allOrNothing = lines[i + 3].split(":")[1].strip() == "True"
                    questions1 = lines[i + 4].strip('"').split('", "')
                    questions2 = lines[i + 5].strip('"').split('", "')
                    questions.append(Matching(qText, [questions1, questions2], allOrNothing, points))
                    i += 6
                else:
                    raise ValueError(f"Invalid question type in quiz.txt at line {i + 1}")
            except (IndexError, ValueError) as e:
                print(f"Error: {e}")
                break
    return Quiz(questions)

def main():
    file_name = "quiz.txt"
    quiz = readQuiz(file_name)
    scores = []
    for question in quiz:
        print("********************************")
        print(question)
        answer = input("Response:\n").split(",")
        score = question.getScore(answer)
        scores.append(score)
        print(f"Score: {score}/{question.getPoints()}")

    print("*********************************")
    print("RESULTS")
    print("*********************************")
    for i, score in enumerate(scores):
        print(f"Q{i + 1} - {score}/{quiz._questions[i].getPoints()}")

    totalScore = sum(scores)
    totalPoints = quiz.getTotalPoints()
    print("*********************************")
    print("TOTAL")
    print("*********************************")
    print(f"RAW: {totalScore}/{totalPoints}")
    print(f"PCT: {(totalScore / totalPoints) * 100:.2f}%")

if __name__ == "__main__":
    main()