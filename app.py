from flask import Flask, render_template, request

app = Flask(__name__)

# Questions (you can add more)
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "C++", "All"],
        "answer": "All"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        score = 0
        
        for i, q in enumerate(quiz):
            user_answer = request.form.get(f"q{i}")
            if user_answer == q["answer"]:
                score += 1

        return render_template("result.html", score=score, total=len(quiz))

    return render_template("index.html", quiz=quiz)


if __name__ == "__main__":
    app.run(debug=True)
