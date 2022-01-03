from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = [Question(question["question"], question["correct_answer"]) for question in question_data]

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()