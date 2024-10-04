from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# creating question bank
question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"],item["answer"]))

# Started quiz
quiz = QuizBrain(question_bank)

# Keep the questions coming till they are over.
while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations! You have completed the quiz.")
print(f"You final score is: {quiz.score}/{len(quiz.question_list)}")