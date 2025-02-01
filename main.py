from flask import Flask, request, render_template

app = Flask(__name__)

# Initialize the text-to-speech engine


@app.route('/', methods=['GET', 'POST'])

def index():
    return render_template('index.html') 


if __name__ == '__main__':
    app.run(port = 4000, debug=True)