from flask import Flask
app = Flask("PaperTrail")

@app.route("/")
def home():
    return "Hello World, from Flask!"