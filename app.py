from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Good(db.Model):
    item_number = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    datecreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Good {self.item_number}>'
    
with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])

def index():
    goods = Good.query.order_by(Good.item).all() 

    if request.method == 'POST':
        try:
            item = request.form['item']
            quantity = int(request.form['quantity'])
            price = float(request.form['price'])

            new_good = Good(item=item, quantity=quantity, price=price)
            db.session.add(new_good)
            db.session.commit()
            return redirect('/')  
        except Exception as e:
            return render_template('index.html', goods=goods, error=f"Error adding good: {e}") 

    return render_template('index.html', goods=goods) 

@app.route('/delete/<int:item_number>')

def delete(item_number):
    deleted_good = Good.query.get_or_404(item_number)

    try:
        db.session.delete(deleted_good)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f'Error deleting good: {e}'

@app.route('/update/<int:item_number>', methods=['GET', 'POST'])
def update(item_number):
    good = Good.query.get_or_404(item_number) 

    if request.method == 'POST':
        try:
            good.item = request.form['item']
            good.quantity = int(request.form['quantity']) 
            good.price = float(request.form['price'])  
            
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Error updating good: {e}" 

    return render_template('update.html', good=good)  

if __name__ == "__main__":
    app.run(debug=True)