
from question_model import Question
from quiz_brain import QuizBrain
from trivia_otazky import trivia_otazky
question_bank = []
for question in trivia_otazky:
    new_text = question["question"]
    new_answer = question["correct_answer"]
    new_question = Question(new_text, new_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
still_has_questions = True
while quiz.still_has_questions():
    quiz.next_question()





