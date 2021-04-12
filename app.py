from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initializing flask app
app = Flask(__name__)

# Configuring database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Making ContactMessage class for database
class ContactMessage(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(120),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    number = db.Column(db.String(15),nullable=False)
    message = db.Column(db.String(500),nullable=False)

# Serving home page to "/"
@app.route("/")
def home():
    return render_template('index.html')

# Serving playlist page to "/playlist"
@app.route("/playlist")
def playlist():
    return render_template('playlist.html')

# Serving contact page to "/contact" and getting contact form post request
@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        pass
    return render_template("contact.html")

# development code
if __name__=='__main__':
    app.run(debug=True)