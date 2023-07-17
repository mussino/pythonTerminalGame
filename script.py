import time

right_answers = 0
wrong_answers = 0

class Question:
    def __init__(self, question, option, answer):
        self.question = question
        self.option = option
        self.answer = answer

q1 = Question('In which country are tuna eyeballs considered a delicacy?', ["\nA. Japan", "B. Brazil", "C. Australia", "D. Singapore\n"], 'A')





#Game starts here:

player_name = input("\nWelcome to the most amazing game you have ever play, would you please write down your name: ")


print("\nThanks for playing with us " + player_name + " we are gonna see a series of questions, if you answer 5 questions wrongs, you are OUT!\n")
time.sleep(5)

input("Are you ready? y/n: ")
print("\n")

print(q1.question)

for options in q1.option:
    print(options)

time.sleep(2)
a1 = input("Your answer is: ")

if a1 == q1.answer:
    right_answers += 1
else:
    wrong_answers += 1



