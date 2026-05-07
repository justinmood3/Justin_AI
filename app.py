from flask import Flask, request, render_template
from ai_engine import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("message")
        if not user_input:
            return "No input provided"

        reply = get_response(user_input)
        return reply

    return "AI Chat is running 🚀"

if __name__ == "__main__":
    app.run()