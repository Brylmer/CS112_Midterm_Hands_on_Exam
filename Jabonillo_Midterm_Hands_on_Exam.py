import random

def generate_question():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operation = random.choice(['+', '-', '*', '/'])
    
    if operation == '+':
        question = "What is " + str(num1) + " + " + str(num2) + "?"
        answer = num1 + num2
    elif operation == '-':
        question = "What is " + str(num1) + " - " + str(num2) + "?"
        answer = num1 - num2
    elif operation == '*':
        question = "What is " + str(num1) + " x " + str(num2) + "?"
        answer = num1 * num2
    else:
        num1 = num2 * random.randint(1, 9)
        question = "What is " + str(num1) + " / " + str(num2) + "?"
        answer = num1 // num2

    return question, answer

def main():
    print("Welcome to the Math Practice Program!")

    while True:
        question, correct_answer = generate_question()
        print(question)

        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                print("Correct!\n")
            else:
                print("Wrong! The correct answer is " + str(correct_answer) + "\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
