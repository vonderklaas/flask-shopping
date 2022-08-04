from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = [
        {
            'id': 1, 
            'name': 'iPhone X', 
            'barcode': '325875634969', 
            'price': '349'
        },
        {
            'id': 2,
            'name': 'Macbook Air M1',
            'barcode': '325875634432', 
            'price': '899'
        },
        {
            'id': 3, 
            'name': 'Razer Blackwidow Keyboard', 
            'barcode': '325875634755', 
            'price': '199'
        }
    ]
    return render_template('market.html', items=items)