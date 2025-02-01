from flask import Flask, request, render_template

app = Flask(__name__)

# Initialize the text-to-speech engine


@app.route('/', methods=['GET', 'POST'])

def index():
    return render_template('index.html') 

#sets up database to be able to be read
#STILL NEEDS EDITTING
db = "database"
col = "collection"

#reads collection document by document
#each document is a dictionary with keys of item and price
def read_database():
    all_entries = col.find({}, "item":1, "price":1)
    for entry in all_entries:
        item = entry["item"]
        price = entry["price"]

#inserts a document into collection
def add_item(item_to_add, price_to_add):
    item = item_to_add
    price = price_to_add
    entry = {"item": item, "price": price}
    col.insert_one(entry)

#delete a document from the collection
def delete_item(item_to_delete):
    entry = {"item": item_to_delete}
    col.delete_one(entry)

if __name__ == '__main__':
    app.run(port = 4000, debug=True)