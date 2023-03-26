from flask import Flask
import os
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)


@app.route('/')

def score_server():

    if os.path.exists(SCORES_FILE_NAME):

        with open(SCORES_FILE_NAME, "r") as score_file:

            results = score_file.readline().strip()
            return "<html><head><title>Scores Game</title></head><body><h1>Hello your score is:<div id='score'>" + results + "</div></h1></body></html>"

    else:
        return "<html><head><title>Scores Game</title></head><body><body><h1><div id='score' style='color:red'>"+BAD_RETURN_CODE+"</div></h1></body></html>"





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
