from flask import Flask
from flask import request
import json


app = Flask(__name__)

scores = []


class Score:
    nick = ""
    points = 0

    def __init__(self, n, p):
        self.nick = n
        self.points = p
        return


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/scores')
def show_scores():
    return json.dumps(sorted(scores, key=lambda sco: sco['points'], reverse=True))


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    content = request.get_json()
    print(content['nick'])
    print(content['points'])
    scores.append(Score(content['nick'], content['points']).__dict__)
    return "Accepted"


scores.append(Score("Artipel", 5).__dict__)
if __name__ == '__main__':
    app.run(debug=True)
