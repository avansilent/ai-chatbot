from flask import Flask, request, jsonify
import requests

app = Flask(__name__)  # ✅ Corrected

OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"  # Ollama local API

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'error': 'Message is required'}), 400

    payload = {
        "model": "mistral",
        "prompt": user_message,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response_data = response.json()
        bot_reply = response_data.get('response', 'No response')

        return jsonify({'reply': bot_reply})

    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to connect to Ollama', 'details': str(e)}), 500

if __name__ == '__main__':  # ✅ Corrected
    app.run(host='0.0.0.0', port=5000, debug=True)
