import json
from flask import Flask, render_template, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data', methods=['POST'])
def get_data():
    value = request.values['current_value']
    wordlist = [line .strip() for line in open('wordlist.txt') if line.startswith(value)]
    response = app.response_class(
        response=json.dumps(wordlist),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/post_data', methods=['POST'])
def post_data():
    print(request.values['text-stuff'])
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
