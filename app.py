from flask import Flask, render_template, request
from ai_engine import get_response
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    global chat_history

    if request.method == "POST":
        user = request.form["message"]
        ai = get_response(user)

        chat_history.append(("You", user))
        chat_history.append(("AI", ai))

    return render_template("index.html", chat=chat_history)

if __name__ == "__main__":
    app.run(debug=True)