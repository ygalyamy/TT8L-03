from flask import Flask, render_template, request
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def bookcover():
    return render_template('cover.html')

@app.route('/edit-book-cover')
def edit_book_cover():
    return render_template('edit_book_cover.html')

if __name__ == '__main__':
    app.run(debug=True)