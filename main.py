from flask import Flask, request, jsonify

app = Flask(__name__)

responses = {
    "hello": "Hi! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing well!",
    "bye": "Goodbye! Have a great day!"
}

@app.route('/chat', methods=['GET'])
def chat():
    user_message = request.args.get('message', '').lower()
    response = responses.get(user_message, "Sorry, I don't understand that.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
