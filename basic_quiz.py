from Question import Question

question_prompts = [
    "What color are apples?\n(a)Red/Green\n(b)Orange",
    "What color are bananas?\n(a)Red/Green\n(b)Yellow",
    "What color are kiwis?\n(a)Green\n(b)Yellow"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got", score, "/", len(questions) + "correct")


run_quiz(questions)
