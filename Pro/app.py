from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = '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'

# List to store chat messages
chat_messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html', messages=chat_messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    if message.strip() != '':
        chat_messages.append({'sender': 'user', 'message': message})
        
        # Generate bot response using OpenAI's GPT-3 API
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message,
            max_tokens=50
        )
        bot_response = response.choices[0].text.strip()
        
        chat_messages.append({'sender': 'bot', 'message': bot_response})
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
