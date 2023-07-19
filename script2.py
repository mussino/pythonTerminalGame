import time

questions = (
    "In which country are tuna eyeballs considered a delicacy?",
    "Where can you dine on a 100-year-old egg?",
    "In which country are fried spiders a popular street food?",
    "Which Queen started the tradition of brides wearing white wedding dresses?",
    "How many birthdays does the Queen of England celebrate?",
    "Where can you have a beer inside a 6,000 year-old tree?",
    "Where can you drink wine and run a marathon at the same time?",
    "Which celebrity wore a meat dress?",
    "Which country created spaghettis, ice cream that looks like spaghetti?",
    "On which island do cats outnumber humans?",
)

options = (
    ("A. Japan", "B. Brazil", "C. Australia", "D. Singapore"),
    ("A. Russia", "B. Finland", "C. China", "D. Estonia"),
    ("A. Ecuador", "B. Peru", "C. Costa Rica", "D. Cambodia"),
    ("A. Queen Victoria", "B. Queen Cleopatra", "C. Mary, Queen of Scots", "D. Catherine the Great"),
    ("A. 3", "B. 2", "C. 1", "D. 0"),
    ("A. Modjadjiskloof", "South Africa", "B. Omsk, Russia", "C. Pokahara, Nepal", "D. Dalat, Vietnam"),
    ("A. Florence, Italy", "B. Paris, France", "C. Budapest, Hungary", "D. Pauillac, France"),
    ("A. Brittney Spears", "B. Katy Perry", "C. Cardi B.", "D. Lady Gaga"),
    ("A. Malta", "B. Italy", "C. Germany", "D. France"),
    ("A. Heigun Island", "B. Ao Island", "C. Iwai Island", "D. Ya Island")
)

answers = ("A", "C", "D", "A", "B", "A", "D", "D", "C", "B")

guesses = []
score = 0
question_num = 0

#Game starts here:

player_name = input("\nWelcome to Triva Quest...would you please write down your name: ")
print("\nThanks for playing with us " + player_name + " we are gonna see a series of questions, if you answer 5 questions wrongs, you are OUT!\n")
time.sleep(5)
input("Are you ready? y/n: ")
print("\n")

for question in questions:
    print("\n--------------------\n")
    print(question)
    print("\n")
    for option in options[question_num]:
        print(option)

    guess = input("\nPlease enter (A, B, C or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("\nCORRECT!\n")
    else:
        print("\nINCORRECT!\n")
        print(f"{answers[question_num]} is the correct answer.") 

    time.sleep(2)
    question_num += 1    


print("--------------------")
print("\n      RESULTS       \n")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"\nYour score was: {score}%\n")
print("--------------------")


