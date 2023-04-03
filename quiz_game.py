def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0
    for i in questions:
        print('-------------------')
        print(i)
        for k in options[question_num]:
            print(k)
        guess = str(input("Enter A, B, C or D: ")).upper()
        if guess not in ("A", "B", "C", "D"):
            print("Wrong value, next question")
            guesses.append('X')
        else:
            guesses.append(guess)
        correct_guesses += check_answer(questions[i], guess)
        question_num += 1
    display_score(correct_guesses, guesses)




def check_answer(answer, guess):
    if answer == guess:
        return 1
    return 0

def display_score(score, guesses):
    print('-------------------')
    print('RESULTS')
    print('-------------------')
    print('Answers: ', end='')
    for i in questions.values():
        print(i, end=' ')
    print()
    print('Guesses: ', end='')
    for k in guesses:
        print(k, end=' ')
    print()
    print("Your score: " + str(int(score/len(questions)*100)) + "%")
    

def play_again():
    while True:
        user_input = input('Wanna play again?: ').upper()
        if user_input == "YES":
            return True
        elif user_input == "NO":
            print('ok byeee')
            return False
        print("Wrong input, try again!")

questions = {
    "Who created Python?: ":"A", 
    "What year was Python created?: ":"B", 
    "Python is tributed to which comedy group?: ":"C", 
    "Is the Earth round?:" :"A"
    }

options = (("A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark"),
           ("A. 1989", "B. 1991", "C. 2000", "D. 2016"),
           ("A. lonely island", "B. Smosh", "C. Monty Python", "D. Snl"),
           ("A. True", "B. False", "C. somethimes", "D. What?"))

if __name__ == "__main__":
    new_game()
    while play_again():
        new_game()