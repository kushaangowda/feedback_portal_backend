from flask import Flask, request
from flask_cors import CORS

import openai

openai.api_key = "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"

app = Flask(__name__)

CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/review", methods=['POST'])
def get_summary():
    data = request.get_json(silent=True)
    comment = data['comment']
    init_text = "Given the message in triple quotes, do the following:\n1. Specify positive phrases in short.\n2. Specify negative phrases in short.\n3. write an assuring and specific response to this customer in 50 words\n"
    prompt = init_text + '""" ' + comment + ' """'
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return [k for k in response["choices"][0]["text"].split("\n") if k!=""]