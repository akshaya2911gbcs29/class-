class invalidoptionerror(Exception):
    pass
class quiz:
    def __init__(self):
        self.question=[]
        self.answer=[]
        self.score=0
    def create_quiz(self):
        n=int(input("Enter the number of questions:"))
        for i in range(n):
            q=input(f"Enter question {i+1}:")
            a=input("option a:")
            b=input("option b:")
            c=input("option c:")
            correct=input("Enter correct option(a/b/c):").upper()
            self.question.append((q,a,b,c))
            self.answer.append(correct)
    def conduct_quiz(self):
        try:
            for i in range(len(self.question)):
                q,a,b,c=self.question[i]
                print(f"\n{q}")
                print("A.",a)
                print("B.",b)
                print("C.",c)
                ans=input("Enter your answer (a/b/c):").upper()
                if ans not in ["A","B","C"]:
                    raise invalidoptionerror("Invalid option selected")
                if ans==self.answer[i]:
                    self.score+=1
            print("Final score:",self.score)
        except invalidoptionerror as e:
            print(e)
quiz=quiz()
quiz.create_quiz()
quiz.conduct_quiz()
