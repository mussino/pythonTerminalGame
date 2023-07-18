import time

class Question:
    def __init__(self, question, option, answer):
        self.question = question
        self.option = option
        self.answer = answer

q1 = Question("In which country are tuna eyeballs considered a delicacy?", ["\nA. Japan", "B. Brazil", "C. Australia", "D. Singapore\n"], "A")
q2 = Question("Where can you dine on a 100-year-old egg?", ["\nA. Russia", "B. Finland", "C. China", "D. Estonia\n"], "C")
q3 = Question("In which country are fried spiders a popular street food?", ["\nA. Ecuador", "B. Peru", "C. Costa Rica", "D. Cambodia\n"], "D")
q4 = Question("Which Queen started the tradition of brides wearing white wedding dresses?", ["\nA. Queen Victoria", "B. Queen Cleopatra", "C. Mary, Queen of Scots", "D. Catherine the Great\n"], "A")
q5 = Question("How many birthdays does the Queen of England celebrate?", ["\nA. 3", "B. 2", "C. 1", "D. 0\n"], "B")
q6 = Question("Where can you have a beer inside a 6,000 year-old tree?", ["\nA. Modjadjiskloof", "South Africa", "B. Omsk, Russia", "C. Pokahara, Nepal", "D. Dalat, Vietnam\n"], "A")
q7 = Question("Where can you drink wine and run a marathon at the same time?", ["\nA. Florence, Italy", "B. Paris, France", "C. Budapest, Hungary", "D. Pauillac, France\n"], "D")
q8 = Question("Which celebrity wore a meat dress?", ["\nA. Brittney Spears", "B. Katy Perry", "C. Cardi B.", "D. Lady Gaga\n"], "D")
q9 = Question("Which country created spaghettis, ice cream that looks like spaghetti?", ["\nA. Malta", "B. Italy", "C. Germany", "D. France\n"], "")
q10 = Question("On which island do cats outnumber humans?", ["\nA. Heigun Island", "B. Ao Island", "C. Iwai Island", "D. Ya Island\n"], "B")


#Game starts here:

player_name = input("\nWelcome to Triva Quest...would you please write down your name: ")
print("\nThanks for playing with us " + player_name + " we are gonna see a series of questions, if you answer 5 questions wrongs, you are OUT!\n")
time.sleep(5)
input("Are you ready? y/n: ")
print("\n")



def question_template(question, option, answer):
    r = 0
    w = 0
    print(question)
    
    for options in option:
        #time.sleep(1.5)
        print(options)
    
    
    #time.sleep(1)
    a = input("You say: ")
    
    if a == answer:
        r += 1
        print("\nYou were right!\n")
        print(r)
    else:
        w += 1
        print("\nYou were wrong...\n")
        print(w)


# Este seria el llamado de la funcion de todas las preguntas, todavia estamos clarificando la funcion:
question_template(q1.question, q1.option, q1.answer)
question_template(q2.question, q2.option, q2.answer)
question_template(q3.question, q3.option, q3.answer)
question_template(q4.question, q4.option, q4.answer)
question_template(q5.question, q5.option, q5.answer)
question_template(q6.question, q6.option, q6.answer)
question_template(q7.question, q7.option, q7.answer)
question_template(q8.question, q8.option, q8.answer)
question_template(q9.question, q9.option, q9.answer)
question_template(q10.question, q10.option, q10.answer)
