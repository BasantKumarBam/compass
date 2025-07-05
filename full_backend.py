
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Home route
@app.route('/', methods=['GET'])
def home():
    return "🎯 Career Compass Backend is Running"

# Greet route
@app.route('/greet', methods=['GET'])
def greet():
    return jsonify({'message': 'Hello from Career Compass!'})

# Simulated Chatbot route (replace with OpenAI later)
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message', '')
    # Simple simulated response
    response = "That's interesting! Tell me more." if user_msg else "Please send a message."
    return jsonify({'reply': response})

# Contact form handler
@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    print(f"Contact from {name} ({email}): {message}")
    return jsonify({'status': 'success', 'message': 'Thank you for contacting us!'})

# Quiz processing route
@app.route('/quiz', methods=['POST'])
def quiz():
    answers = request.json.get('answers', [])
    # Dummy logic: Recommend based on first answer
    if not answers:
        return jsonify({'suggestedCareer': 'Please complete the quiz.'})
    if 'science' in answers[0].lower():
        career = 'Doctor or Engineer'
    elif 'business' in answers[0].lower():
        career = 'Manager or Entrepreneur'
    else:
        career = 'Teacher or Designer'
    return jsonify({'suggestedCareer': career})

# Run server
if __name__ == '__main__':
    app.run(debug=True)
