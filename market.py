from flask import Flask, render_template

# Refer to local .py file
app = Flask(__name__)

# Routes
@app.route("/")
def home_page():
    return render_template('home.html')
