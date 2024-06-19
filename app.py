from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data for demonstration
users = {
    "user@example.com": "password123"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email in users and users[email] == password:
        session['email'] = email
        return redirect(url_for('webpage'))
    else:
        return "Invalid credentials. Please try again."

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Add basic validation for empty fields and existing users
        if not email or not password:
            return "Please provide both email and password."
        if email in users:
            return "User already exists."

        # Add the new user
        users[email] = password
        return redirect(url_for('index'))
    
    return render_template('signup.html')

@app.route('/webpage')
def webpage():
    if 'email' in session:
        return render_template('webpage.html')
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)