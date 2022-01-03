from question_model import Question


class QuizBrain:

    def __init__(self, questionList):
        self.questionNumber = 0
        self.questionList = questionList
        self.score = 0

    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionList)

    def nextQuestion(self):
        userAns = input("Q" + str(self.questionNumber + 1) + ": " + self.questionList[self.questionNumber].text + " (True/False)?: ")
        self.checkAnswer(userAns, self.questionList[self.questionNumber].answer)
        self.questionNumber += 1

    def checkAnswer(self, userAns, correctAns):
        if userAns.lower() == correctAns.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print("The correct answer was " + correctAns + ".")
        print(f"Current score is {self.score}/{self.questionNumber + 1}.")
        print("\n")

        if self.questionNumber == len(self.questionList) - 1:
            print("\n")
            print("You have completed the quiz!")
            print(f"Your final score is {self.score}/{self.questionNumber + 1}!")
