from flask import Flask, render_template, request, redirect, url_for, session, flash
from forms import LoginForm as WTLoginForm  # Renamed the imported LoginForm
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length
import dataset
import hashlib

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'

# Connect to the SQLite database
db = dataset.connect('sqlite:///database.db')

# Define the 'users' table
table = db['users']

# Routes
@app.route('/')
def home():
    return render_template('webpage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = WTLoginForm()  # Create an instance of the LoginForm class
    if request.method == 'POST' and form.validate_on_submit():
        # Registration logic here
        username = form.username.data
        password = hashlib.sha256(form.password.data.encode()).hexdigest()  # Hash the password
        table.insert(dict(username=username, password=password))
        return redirect(url_for('login'))  # Redirect to the login page after successful registration
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = WTLoginForm()  # Create an instance of the LoginForm class
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = hashlib.sha256(form.password.data.encode()).hexdigest()  # Hash the password
        user = table.find_one(username=username, password=password)
        if user:
            session['username'] = username  # Store username in session
            return redirect(url_for('home'))  # Redirect to homepage after successful login
        else:
            flash('Invalid username or password')  # Show error message
    return render_template('login.html', form=form)  # Pass the form to the login.html template

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return render_template('dashboard.html')  # Render dashboard if logged in

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)