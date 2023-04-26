# Import required libraries
from flask import Flask, render_template, request, jsonify
import openai
import os
import signal

# Initialize Flask app
app = Flask(__name__)

# Function to chat with GPT
def chat_with_gpt(prompt):
    openai.organization = os.getenv('OPENAI_ORG_ID')
    openai.api_key = os.getenv('OPENAI_API_KEY')

    messages = [
        {"role": "system", "content": "You are a super helpful AI assistant. You will always find a way to answer "
         "the questions you are asked. If you do not know the answer you will answer truthfully that you do not know"},
        {"role": "user", "content": prompt}
        ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1
    )

    return response.choices[0].message['content'].strip()

# Route for the homepage
@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data['prompt']
        response = chat_with_gpt(prompt)
        return jsonify({"response": response})
    return jsonify({"message": "This endpoint only accepts POST requests with JSON data."})
    
# Quit routine
@app.route('/quit', methods=['POST'])
def quit():
    os.kill(os.getpid(), signal.SIGTERM)  # Terminate the Flask app
    return 'Server shutting down...', 200

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
