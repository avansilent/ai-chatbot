from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your chatbot!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    # Extract intent name from Dialogflow request
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

    # Handle different intents
    response_text = "I didn't understand that."

    if intent_name == "Welcome Intent":
        response_text = "Hello! How can I assist you today?"
    elif intent_name == "Goodbye Intent":
        response_text = "Goodbye! Have a great day!"
    elif intent_name == "Your Custom Intent":
        response_text = "Your custom response here."

    # JSON response format for Dialogflow
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
