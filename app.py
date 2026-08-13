from flask import Flask, render_template, request, jsonify
from chatbot_logic import handle_query

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"reply": "Please type a question."}), 400

        response = handle_query(user_message, context={})
        return jsonify({"reply": response})

    except Exception as error:
        print(f"Error: {error}")
        return jsonify({"reply": "Sorry, something went wrong. Please try again."}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
