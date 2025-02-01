from flask import Flask, request, render_template
from flask_pymongo import PyMongo
import requests
import pyttsx3



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://grhackru:dbgrhackRU@cluster.mongodb.net/todo_db"
mongo = PyMongo(app)
engine = pyttsx3.init()

@app.route('/', methods=['GET','POST'])

def index():
    if request.method == 'POST':
        name = request.form['name']
        r = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}')
        data = r.json()
        if data.get("meals"):
            mealnames = [meal["strMeal"] for meal in data["meals"]]
        return "No meals found."
    return render_template('index.html')
    


if __name__ == '__main__':
    app.run(port = 4000, debug=True)
