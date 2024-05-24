from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('text size customizable.html')

@app.route('/customize', methods=['POST'])
def customize():
    text_size = request.form['text_size']
    return render_template('text size customizable.html', text_size=text_size)

if __name__ == '__main__':
    app.run(debug=True)
