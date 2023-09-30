class QuizBrain:
    def __init__(self,q_list) -> None:
        self.question_number=0
        self.question_list=q_list
        self.score=0 

    def still_have_question(self):
        leng=len(self.question_list)#12
        return self.question_number<leng
    
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        answer=input(f"Q.{self.question_number}: {current_question.text}? (True/False):")
        self.check_answer(answer,current_question.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You Got it Right!")
            self.score+=1
            
        else:
            print("Thats Wrong")
        print(f"The Correct Answer Was: {correct_answer}")
        print(f"Your Score :{self.score}/{self.question_number}")
        print("\n")
        