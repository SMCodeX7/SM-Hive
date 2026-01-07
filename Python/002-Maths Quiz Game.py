import random

print("Welcome To Maths Quiz")

player_name = input("Enter your name : ")

player_name = player_name.strip()
player_name = player_name.capitalize()

print(f"\nHey {player_name} Get Ready For The Quiz")

play_again = "yes"

while play_again == "yes":
    score = 0
    question_number = 1

    while question_number <= 10:
        num1 = random.randint(1,21)
        num2 = random.randint(1,21)

        operation_number = random.randint(1,4)

        if operation_number == 1:
            operator = "+"
            answer = num1 + num2
        elif operation_number == 2:
            operator = "-"
            answer = num1 - num2
        elif operation_number == 3:
            operator = "*"
            answer = num1 * num2
        else:
            operator = "**"
            answer = num1 ** num2
        
        print(f"Question {question_number}: {num1} {operator} {num2} = ?")
        user_answer = int(input(f"Question {question_number}'s Answer : "))
        
        if answer == user_answer:
            score += 1
        else:
            print(f"Correct Answer For Question {question_number} : {answer}")
        
        question_number += 1

    score_percentage = (score/10) * 100

    print(f"Quiz Completed : Your Score -- {score}/10 , Your Percentage -- {score_percentage:.1f}%")

    if score_percentage >= 90:
        print("A - Excellent")
    elif score_percentage >= 80:
        print("B - Very Good")
    elif score_percentage >= 70:
        print("C - Good")
    elif score_percentage >= 60:
        print("D - Needs Practice")
    else:
        print("F - Keep Trying")

    while True:
        play_again = input("\nPlay Again? (yes / no) : ")
        play_again = play_again.lower().strip()
        
        if play_again == "yes" or play_again == "no":
            break
        else:
            print("Please type 'yes' or 'no' only!")
    
    if play_again == "yes":
        print("\n" + "="*50)
        print("STARTING NEW QUIZ WITH NEW QUESTIONS!!!")
        print("="*50)

print("\nThanks for playing! Goodbye!")
