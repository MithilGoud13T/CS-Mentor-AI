from flask import Flask, render_template, request, jsonify
from chatbotai import ask_mentor

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}

    message = data.get("message", "")
    mode = data.get("mode", "Learn Concept")
    history = data.get("history", [])

    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "Please enter a question."}), 400

    if not isinstance(mode, str):
        mode = "Learn Concept"

    if not isinstance(history, list):
        history = []

    answer = ask_mentor(message, mode, history)

    return jsonify({"response": answer})


@app.route("/api/health")
def health():
    return jsonify({
        "status": "running",
        "model": "llama3.2:latest"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)