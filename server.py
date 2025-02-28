from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Hello, this is your AI chatbot!"

# Example API endpoint (Modify as needed)
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json  # Get JSON data from request
    user_message = data.get("message", "")

    # Example response (Replace with AI chatbot logic)
    bot_response = f"You said: {user_message}"
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Ensure it runs on all addresses
