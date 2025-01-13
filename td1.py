# This function asks the question and compares the answer with the correct one
def ask_question(question, correct_answer):
    # Prompt the user for input and compare the answer case-insensitively
    answer = input(f"{question} ")  # Ask the user a question
    if answer.lower() == correct_answer.lower():  # Compare the answer
        print("Correct!")  # If the answer is right
        return True  # Return True for a correct answer
    else:
        print("Wrong!")  # If the answer is wrong
        return False  # Return False for a wrong answer

# Main function to control the flow of the quiz
def main():
    # List of questions and their correct answers
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is 5 + 7?", "12"),
        ("Who wrote 'Hamlet'?", "Shakespeare"),
    ]
    
    # Initialize the score to 0
    score = 0
    
    # Loop through the list of questions
    for question, correct_answer in questions:
        if ask_question(question, correct_answer):  # Ask each question
            score += 1  # Increase score if the answer is correct
    
    # Display the total score at the end of the quiz
    print(f"You got {score}/{len(questions)} correct!")

# This part ensures the code runs when executed as a script, but not if it's imported as a module
if __name__ == "__main__":
    main()
