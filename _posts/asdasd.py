metadata = {
    "toc": True,
    "comments": False,
    "layout": "post",
    "title": "Python Quiz",
    "description": "Math Quiz",
    "type": "hacks",
    "courses": {
        "compsci": {
            "week": 3
        }
    }
}
import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-"])
    if operator == "+":
        answer = num1 + num2
    else:
        answer = num1 - num2
    question = f"What is {num1} {operator} {num2}?"
    return question, answer

def main():
    num_questions = 5
    correct_answers = 0
    
    print("Welcome to the Math Quiz!")
    
    for _ in range(num_questions):
        question, correct_answer = generate_question()
        print(question)
        user_answer = input("Your answer: ")
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if user_answer == correct_answer:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Wrong. The correct answer is {correct_answer}\n")
    
    print(f"You got {correct_answers} out of {num_questions} questions correct.")
    if correct_answers == num_questions:
        print("Congratulations!")

if __name__ == "__main__":
    main()
