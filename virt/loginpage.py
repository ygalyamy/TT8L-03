from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

#def index():
#    return "<hl>Welcome to PaperTrail!</h1>"

def index():
    return render_template("index.html")

# localhost:5000/user/alya
@app.route('/user/<name>')

def user(name):
    return "<hl>Hello {}!!</h1>".format(name)

if __name__ == '__main__':
    app.run(debug=True)