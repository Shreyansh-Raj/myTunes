from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

# Initializing flask app
app = Flask(__name__)
app.secret_key = "abc" 
# Configuring database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Making ContactMessage class for database
class ContactMessage(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(120),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    phone_number = db.Column(db.String(15),nullable=False)
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
    # Adding form data to database when user send post request
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['number']
        message = request.form['message']
        element = ContactMessage(user_name=name,email=email,phone_number=phone,message=message)
        db.session.add(element)
        db.session.commit()

        flash("Message Sent!")
    return render_template("contact.html")

# Serving admin page for viewing contact messages
@app.route("/admin",methods=['GET','POST'])
def admin():
    # Checking admin user and password
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Serving admin.html if email and password are correct
        if email == 'hrishiraj1570@gmail.com' and password == 'Shreyansh$9128':
            messages = ContactMessage.query.all()
            return render_template('admin.html',messages=messages)
        
        # Reloading page if email and passwordare incorrect
        else:
            return redirect('/admin')

    return render_template("login.html")

# Making delete function to delete contact messages
@app.route("/delete/<int:sno>")
def delete(sno):
    # Deleting entry
    entry = ContactMessage.query.filter_by(sno=sno).first()
    db.session.delete(entry)
    db.session.commit()
    return redirect('/admin')

if __name__=='__main__':
    app.run()