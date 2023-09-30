from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]

for item in question_data:
    text=item["question"]
    ans=item["correct_answer"]
    question=Question(text,ans)
    question_bank.append(question)

quiz=QuizBrain(question_bank) 

while quiz.still_have_question():
    quiz.next_question()

print("Youve completed the quiz")

print(f"Your final score was {quiz.score}/{quiz.question_number}")