from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    qeustion_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(qeustion_text, question_answer)
    question_bank.append(new_question)

print(question_bank[0].answer)