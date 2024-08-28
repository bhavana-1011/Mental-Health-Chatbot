from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define a set of responses for the chatbot
pairs = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hi there! What can I do for you?']),
    (r'what is your name?', ['I am a mental health chatbot.', 'You can call me Chatbot.']),
    (r'how are you?', ['I am just a program, but I am here to help you.', 'I am here and ready to assist you.']),
    (r'I need help with my mental situation', ['I am here to help with %1. Can you provide more details?']),
    (r'I am feeling very down', ['I am sorry to hear that you are feeling %1. Talking to someone might help.']),
    (r'Ok thank you', ['Goodbye! Take care.']),
]

# Initialize the chatbot with pairs and reflections
chatbot = Chat(pairs, reflections)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_input = request.args.get('msg')
    response = chatbot.respond(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
