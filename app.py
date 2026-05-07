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
        user_input = request.form.get("message")

        if not user_input:
            return render_template("index.html", chat=chat_history)

        reply = get_response(user_input)

        chat_history.append(("You", user_input))
        chat_history.append(("AI", reply))

    return render_template("index.html", chat=chat_history)

@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json()

    if not data or "message" not in data:
        return {"error": "No message provided"}, 400

    reply = get_response(data["message"])

    return {"reply": reply}

if __name__ == "__main__":
    app.run()