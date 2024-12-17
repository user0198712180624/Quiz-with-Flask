from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions =[
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Mars", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is my name?",
        "options": ["Unika Ghimire", "Unika", "g.yyunika", "Yunika"],
        "answer": "Unika Ghimire"
    },
    {
        "question": "Who is the best player in the world'?",
        "options": ["Messi", "Lionel Messi", "Lionel Andres Messi", "Leo"],
        "answer": "Lionel Andres Messi"
    },
    {
        "question": "What is my favourite color?'?",
        "options": ["None", "Red", "Pink", "Black"],
        "answer": "None"
    }
 ]


@app.route("/")
def home():
    return redirect(url_for("quiz", question_id=0))

@app.route("/quiz/<int:question_id>", methods=["GET", "POST"])
def quiz(question_id):
    if request.method == "POST":
        user_answer = request.form.get("answer")
        correct_answer = questions[question_id]["answer"]
        if user_answer == correct_answer:
            message = "Correct!"
        else:
            message = "Wrong answer."

        # If there are more questions, redirect to the next question
        if question_id + 1 < len(questions):
            return redirect(url_for("quiz", question_id=question_id + 1))
        else:
            # Quiz is complete
            return render_template("result.html", message=message, score=question_id + 1)

    # Render the current question
    if question_id < len(questions):
        question = questions[question_id]
        return render_template("quiz.html", question=question, question_id=question_id)
    else:
        return render_template("result.html", score=len(questions))

if __name__ == "__main__":
    app.run(debug=True)


