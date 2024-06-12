from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import base64
from datetime import datetime
import json

app = Flask(__name__)

if not os.path.exists('static/images'):
    os.makedirs('static/images')

@app.route('/')
def bookcover(): 
    image_path = 'images/bookcover.png'
    image_exists = os.path.exists(os.path.join('static', image_path))
    return render_template('cover.html', image_exists=image_exists, image_path=image_path)

@app.route('/edit-book-cover', methods=['GET'])
def edit_book_cover():
    return render_template('edit_book_cover.html')

@app.route('/save_image', methods=['POST'])
def save_image():
    data = request.json
    image_data = data['image'].split(",")[1]
    image_data = base64.b64decode(image_data)
    with open('static/images/bookcover.png', 'wb') as f:
        f.write(image_data)
    
    with open('static/images/canvas_state.json', 'w') as f:
        json.dump(data['canvasState'], f)

    return jsonify(success=True)

@app.route('/load_canvas_state', methods=['GET'])
def load_canvas_state():
    canvas_state_path = 'static/images/canvas_state.json'
    if os.path.exists(canvas_state_path):
        with open(canvas_state_path, 'r') as f:
            canvas_state = json.load(f)
        return jsonify(success=True, canvasState=canvas_state)
    return jsonify(success=False, message="No canvas state found.")

@app.route('/notification')
def noti():
    return render_template("notification.html")

@app.route('/book-of-the-month')
def bookofthemonth():
    return render_template("book_of_the_month.html")

@app.route('/index')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)