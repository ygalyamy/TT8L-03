from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import base64
from datetime import datetime
import json

app = Flask(__name__)

if not os.path.exists('static/images'):
    os.makedirs('static/images')

FICTION_IMAGE_PATH = 'static/images/bookcover.png'
COMEDY_IMAGE_PATH = 'static/images/bookcover2.png'
OTHERS_IMAGE_PATH = 'static/images/bookcover3.png'
ROMANCE_IMAGE_PATH = 'static/images/bookcover4.png'
THRILLER_IMAGE_PATH = 'static/images/bookcover5.png'
HORROR_IMAGE_PATH = 'static/images/bookcover6.png'
MANGA_IMAGE_PATH = 'static/images/bookcover7.png'
NONFICTION_IMAGE_PATH = 'static/images/bookcover8.png'
CANVAS_STATE_PATH = 'static/images/canvas_state.json'
COMEDY_CANVAS_STATE_PATH = 'static/images/comedy_canvas_state.json'
OTHERS_CANVAS_STATE_PATH = 'static/images/others_canvas_state.json'
ROMANCE_CANVAS_STATE_PATH = 'static/images/romance_canvas_state.json'
THRILLER_CANVAS_STATE_PATH = 'static/images/thriller_canvas_state.json'
HORROR_CANVAS_STATE_PATH = 'static/images/horror_canvas_state.json'
MANGA_CANVAS_STATE_PATH = 'static/images/manga_canvas_state.json'
NONFICTION_CANVAS_STATE_PATH = 'static/images/nonfiction_canvas_state.json'

@app.route('/edit-book-cover', methods=['GET'])
def edit_book_cover():
    return render_template('edit_book_cover.html')

@app.route('/comedy_edit_book_cover', methods=['GET'])
def comedy_edit_book_cover():
    return render_template('comedy_edit_book_cover.html')

@app.route('/others_edit_book_cover', methods=['GET'])
def others_edit_book_cover():
    return render_template('others_edit_book_cover.html')

@app.route('/romance_edit_book_cover', methods=['GET'])
def romance_edit_book_cover():
    return render_template('romance_edit_book_cover.html')

@app.route('/thriller_edit_book_cover', methods=['GET'])
def thriller_edit_book_cover():
    return render_template('thriller_edit_book_cover.html')

@app.route('/horror_edit_book_cover', methods=['GET'])
def horror_edit_book_cover():
    return render_template('horror_edit_book_cover.html')

@app.route('/manga_edit_book_cover', methods=['GET'])
def manga_edit_book_cover():
    return render_template('manga_edit_book_cover.html')

@app.route('/nonfiction_edit_book_cover', methods=['GET'])
def nonfiction_edit_book_cover():
    return render_template('nonfiction_edit_book_cover.html')

@app.route('/save_comedy_image', methods=['POST'])
def save_comedy_image():
    try:
        data = request.json
        image_data = data['image'].split(",")[1]
        image_data = base64.b64decode(image_data)

        with open(COMEDY_IMAGE_PATH, 'wb') as f:
            f.write(image_data)

        with open(COMEDY_CANVAS_STATE_PATH, 'w') as f:
            json.dump(data['canvasState'], f)

        return jsonify(success=True, image_path=COMEDY_IMAGE_PATH)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/load_comedy_canvas_state', methods=['GET'])
def load_comedy_canvas_state():
    try:
        if os.path.exists(COMEDY_CANVAS_STATE_PATH):
            with open(COMEDY_CANVAS_STATE_PATH, 'r') as f:
                comedy_canvas_state = json.load(f)
            return jsonify(success=True, canvasState=comedy_canvas_state)
        return jsonify(success=False, message="No comedy canvas state found.")
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/save_others_image', methods=['POST'])
def save_others_image():
    try:
        data = request.json
        image_data = data['image'].split(",")[1]
        image_data = base64.b64decode(image_data)

        with open(OTHERS_IMAGE_PATH, 'wb') as f:
            f.write(image_data)

        with open(OTHERS_CANVAS_STATE_PATH, 'w') as f:
            json.dump(data['canvasState'], f)

        return jsonify(success=True, image_path=OTHERS_IMAGE_PATH)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/load_others_canvas_state', methods=['GET'])
def load_others_canvas_state():
    try:
        if os.path.exists(OTHERS_CANVAS_STATE_PATH):
            with open(OTHERS_CANVAS_STATE_PATH, 'r') as f:
                others_canvas_state = json.load(f)
            return jsonify(success=True, canvasState=others_canvas_state)
        return jsonify(success=False, message="No others canvas state found.")
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/save_romance_image', methods=['POST'])
def save_romance_image():
    try:
        data = request.json
        image_data = data['image'].split(",")[1]
        image_data = base64.b64decode(image_data)

        with open(ROMANCE_IMAGE_PATH, 'wb') as f:
            f.write(image_data)

        with open(ROMANCE_CANVAS_STATE_PATH, 'w') as f:
            json.dump(data['canvasState'], f)

        return jsonify(success=True, image_path=ROMANCE_IMAGE_PATH)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/load_romance_canvas_state', methods=['GET'])
def load_romance_canvas_state():
    try:
        if os.path.exists(ROMANCE_CANVAS_STATE_PATH):
            with open(ROMANCE_CANVAS_STATE_PATH, 'r') as f:
                romance_canvas_state = json.load(f)
            return jsonify(success=True, canvasState=romance_canvas_state)
        return jsonify(success=False, message="No others canvas state found.")
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/save_thriller_image', methods=['POST'])
def save_thriller_image():
    try:
        data = request.json
        image_data = data['image'].split(",")[1]
        image_data = base64.b64decode(image_data)

        with open(THRILLER_IMAGE_PATH, 'wb') as f:
            f.write(image_data)

        with open(THRILLER_CANVAS_STATE_PATH, 'w') as f:
            json.dump(data['canvasState'], f)

        return jsonify(success=True, image_path=THRILLER_IMAGE_PATH)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/load_thriller_canvas_state', methods=['GET'])
def load_thriller_canvas_state():
    try:
        if os.path.exists(THRILLER_CANVAS_STATE_PATH):
            with open(THRILLER_CANVAS_STATE_PATH, 'r') as f:
                thriller_canvas_state = json.load(f)
            return jsonify(success=True, canvasState=thriller_canvas_state)
        return jsonify(success=False, message="No others canvas state found.")
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/save_horror_image', methods=['POST'])
def save_horror_image():
    try:
        data = request.json
        image_data = data['image'].split(",")[1]
        image_data = base64.b64decode(image_data)

        with open(HORROR_IMAGE_PATH, 'wb') as f:
            f.write(image_data)

        with open(HORROR_CANVAS_STATE_PATH, 'w') as f:
            json.dump(data['canvasState'], f)

        return jsonify(success=True, image_path=HORROR_IMAGE_PATH)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/load_horror_canvas_state', methods=['GET'])
def load_horror_canvas_state():
    try:
        if os.path.exists(HORROR_CANVAS_STATE_PATH):
            with open(HORROR_CANVAS_STATE_PATH, 'r') as f:
                horror_canvas_state = json.load(f)
            return jsonify(success=True, canvasState=horror_canvas_state)
        return jsonify(success=False, message="No others canvas state found.")
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/save_manga_image', methods=['POST'])
def save_manga_image():
    try:
        data = request.json
        image_data = data['image'].split(",")[1]
        image_data = base64.b64decode(image_data)

        with open(MANGA_IMAGE_PATH, 'wb') as f:
            f.write(image_data)

        with open(MANGA_CANVAS_STATE_PATH, 'w') as f:
            json.dump(data['canvasState'], f)

        return jsonify(success=True, image_path=MANGA_IMAGE_PATH)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/load_manga_canvas_state', methods=['GET'])
def load_manga_canvas_state():
    try:
        if os.path.exists(MANGA_CANVAS_STATE_PATH):
            with open(MANGA_CANVAS_STATE_PATH, 'r') as f:
                manga_canvas_state = json.load(f)
            return jsonify(success=True, canvasState=manga_canvas_state)
        return jsonify(success=False, message="No others canvas state found.")
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/save_nonfiction_image', methods=['POST'])
def save_nonfiction_image():
    try:
        data = request.json
        image_data = data['image'].split(",")[1]
        image_data = base64.b64decode(image_data)

        with open(NONFICTION_IMAGE_PATH, 'wb') as f:
            f.write(image_data)

        with open(NONFICTION_CANVAS_STATE_PATH, 'w') as f:
            json.dump(data['canvasState'], f)

        return jsonify(success=True, image_path=NONFICTION_IMAGE_PATH)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/load_nonfiction_canvas_state', methods=['GET'])
def load_nonfiction_canvas_state():
    try:
        if os.path.exists(NONFICTION_CANVAS_STATE_PATH):
            with open(NONFICTION_CANVAS_STATE_PATH, 'r') as f:
                nonfiction_canvas_state = json.load(f)
            return jsonify(success=True, canvasState=nonfiction_canvas_state)
        return jsonify(success=False, message="No others canvas state found.")
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/save_image', methods=['POST'])
def save_image():
    try:
        data = request.json
        genre = request.args.get('genre', 'fiction')  # Get genre from query parameter

        if genre == 'fiction':
            image_path = FICTION_IMAGE_PATH
            canvas_state_path = CANVAS_STATE_PATH
        elif genre == 'comedy':
            image_path = COMEDY_IMAGE_PATH
            canvas_state_path = COMEDY_CANVAS_STATE_PATH
        elif genre == 'others':
            image_path = OTHERS_IMAGE_PATH
            canvas_state_path = OTHERS_CANVAS_STATE_PATH
        elif genre == 'romance':
            image_path = ROMANCE_IMAGE_PATH
            canvas_state_path = ROMANCE_CANVAS_STATE_PATH
        elif genre == 'thriller':
            image_path = THRILLER_IMAGE_PATH
            canvas_state_path = THRILLER_CANVAS_STATE_PATH
        elif genre == 'horror':
            image_path = THRILLER_IMAGE_PATH
            canvas_state_path = HORROR_CANVAS_STATE_PATH
        elif genre == 'manga':
            image_path = MANGA_IMAGE_PATH
            canvas_state_path = MANGA_CANVAS_STATE_PATH
        elif genre == 'nonfiction':
            image_path = NONFICTION_IMAGE_PATH
            canvas_state_path = NONFICTION_CANVAS_STATE_PATH
        else:
            return jsonify(success=False, error='Invalid genre provided')

        image_data = data['image'].split(",")[1]
        image_data = base64.b64decode(image_data)

        with open(image_path, 'wb') as f:
            f.write(image_data)

        with open(CANVAS_STATE_PATH, 'w') as f:
            json.dump(data['canvasState'], f)

        return jsonify(success=True, image_path=image_path)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/load_canvas_state', methods=['GET'])
def load_canvas_state():
    try:
        genre = request.args.get('genre', 'fiction')  # Get genre from query parameter

        if genre == 'fiction':
            canvas_state_path = CANVAS_STATE_PATH
        elif genre == 'comedy':
            canvas_state_path = COMEDY_CANVAS_STATE_PATH
        elif genre == 'others':
            canvas_state_path = OTHERS_CANVAS_STATE_PATH
        elif genre == 'romance':
            canvas_state_path = ROMANCE_CANVAS_STATE_PATH
        elif genre == 'thriller':
            canvas_state_path = THRILLER_CANVAS_STATE_PATH
        elif genre == 'horror':
            canvas_state_path = HORROR_CANVAS_STATE_PATH
        elif genre == 'manga':
            canvas_state_path = MANGA_CANVAS_STATE_PATH
        elif genre == 'nonfiction':
            canvas_state_path = NONFICTION_CANVAS_STATE_PATH
        else:
            return jsonify(success=False, message="Invalid genre provided.")

        if os.path.exists(CANVAS_STATE_PATH):
            with open(CANVAS_STATE_PATH, 'r') as f:
                canvas_state = json.load(f)
            return jsonify(success=True, canvasState=canvas_state)
        return jsonify(success=False, message="No canvas state found.")
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/notification')
def noti():
    return render_template("notification.html")

@app.route('/book-of-the-month')
def bookofthemonth():
    return render_template("book_of_the_month.html")

@app.route('/submit-review', methods=['POST'])
def submit_review():
    try:
        data = request.json  # Assuming data is sent as JSON
        genre = request.referrer.split('/')[-1].split('.')[0]  # Get the HTML file name (genre)
        
        # Add review to appropriate genre in dictionary
        reviews[genre].append(data)

        # Optionally, you can store reviews in local storage or database here

        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/fetch-reviews')
def fetch_reviews():
    try:
        genre = 'fiction'  # Replace with dynamic genre extraction logic if needed
        return jsonify(success=True, reviews=reviews[genre])
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/fiction')
def fiction():
    return render_template("fiction.html")

@app.route('/fiction-book-reviews')
def fictionreviews():
    return render_template("fictionlayout.html")

@app.route('/comedy')
def comedy():
    return render_template("comedy.html")

@app.route('/comedy-book-reviews')
def comedyreviews():
    return render_template("comedylayout.html")

@app.route('/others')
def others():
    return render_template("others.html")

@app.route('/others-book-reviews')
def othersreviews():
    return render_template("otherslayout.html")

@app.route('/romance')
def romance():
    return render_template("romance.html")

@app.route('/romance-book-reviews')
def romancereviews():
    return render_template("romancelayout.html")

@app.route('/thriller')
def thriller():
    return render_template("thriller.html")

@app.route('/thriller-book-reviews')
def thrillerreviews():
    return render_template("thrillerlayout.html")

@app.route('/horror')
def horror():
    return render_template("horror.html")

@app.route('/horror-book-reviews')
def horrorreviews():
    return render_template("horrorlayout.html")

@app.route('/manga')
def manga():
    return render_template("comics-manga.html")

@app.route('/manga-book-reviews')
def mangareviews():
    return render_template("mangalayout.html")

@app.route('/nonfiction')
def nonfiction():
    return render_template("non-fiction.html")

@app.route('/nonfiction-book-reviews')
def nonfictionreviews():
    return render_template("nonfictionlayout.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)