# Smart Auto Quiz Game in Python

def run_quiz(questions):
    score = 0
    print("\n🎯 Welcome to the Quiz Game!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for option in q['options']:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {q['answer']}\n")

    print("🎮 Quiz Completed!")
    print(f"🏁 Final Score: {score}/{len(questions)}")

    if score == len(questions):
        print("🏆 Excellent! Full marks!")
    elif score >= len(questions) // 2:
        print("👍 Good effort!")
    else:
        print("📚 Keep practicing!")

# List of questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Pune"],
        "answer": "B"
    },
    {
        "question": "Which language is used for styling web pages?",
        "options": ["A) HTML", "B) CSS", "C) JavaScript", "D) Python"],
        "answer": "B"
    },
    {
        "question": "Which year did India get independence?",
        "options": ["A) 1945", "B) 1946", "C) 1947", "D) 1950"],
        "answer": "C"
    },
    {
        "question": "Which of these is a programming language?",
        "options": ["A) Snake", "B) Java", "C) Google", "D) Chrome"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A) Central Processing Unit", "B) Control Panel Unit", "C) Computer Power Unit", "D) Control Power Unit"],
        "answer": "A"
    },
    {
        "question": "Which planet is closest to the sun?",
        "options": ["A) Venus", "B) Earth", "C) Mercury", "D) Mars"],
        "answer": "C"
    },
    {
        "question": "Which data structure uses FIFO?",
        "options": ["A) Stack", "B) Queue", "C) Tree", "D) Graph"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A) //", "B) --", "C) #", "D) <!--"],
        "answer": "C"
    },
    {
        "question": "HTML stands for?",
        "options": ["A) HighText Machine Language", "B) HyperText and links Markup Language", "C) HyperText Markup Language", "D) None of these"],
        "answer": "C"
    },
    {
        "question": "Which of the following is not a database?",
        "options": ["A) MySQL", "B) Oracle", "C) GitHub", "D) PostgreSQL"],
        "answer": "C"
    }
]

# Run the quiz
run_quiz(questions)
