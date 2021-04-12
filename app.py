from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initializing flask app
app = Flask(__name__)

# Configuring database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ContactMessage(db.Model):
    pass

# Serving home page to "/"
@app.route("/")
def home():
    return render_template('index.html')

# Serving playlist page to "/playlist"
@app.route("/playlist")
def playlist():
    return render_template('playlist.html')

# Serving contact page to "/contact"
@app.route("/contact")
def contact():
    return render_template("contact.html")

# development code
if __name__=='__main__':
    app.run(debug=True)