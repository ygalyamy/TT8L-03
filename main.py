from flask import Flask, render_template, request, redirect, url_for,jsonify
import os
import base64

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
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)