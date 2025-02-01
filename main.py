from flask import Flask, request, render_template
import pyttsx3
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def translate_text(string):
    return GoogleTranslator(source="auto",target="es").translate(string)


@app.route('/work', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        name = request.form['name']
        text = translate_text(name)
        engine.say(text)  # Queue the text
        engine.runAndWait()  # Speak the text
        return f'{text}! '
    return render_template('index.html') 


if __name__ == '__main__':
    app.run(port = 4000, debug=True)
