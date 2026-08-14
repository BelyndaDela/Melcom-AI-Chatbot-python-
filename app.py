from flask import Flask, render_template, request, jsonify
from chatbot_logic import handle_query

app = Flask(__name__)

# Store conversation context
context = {}


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}

    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({
            "reply": "Please type a message so I can help you."
        })

    response = handle_query(
        user_input,
        context=context
    )

    return jsonify({
        "reply": response
    })


if __name__ == "__main__":
    app.run(debug=True)