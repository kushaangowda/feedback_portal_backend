from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import json_util
import openai
import os
from dotenv import load_dotenv
load_dotenv()

mongo = PyMongo()


openai.api_key = os.getenv("OPEN_API_KEY")

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv("MONGO_URI")

mongo.init_app(app)
db = mongo.db

CORS(app)

def getGPTResponse(prompt):
    return openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=500)["choices"][0]["text"]

def get_summary(comment):
    init_text1 = "Given the message in triple quotes, Specify positive phrases in short.\n"
    init_text2 = "Given the message in triple quotes, Specify negative phrases in short.\n"
    init_text3 = "Given the message in triple quotes, write an assuring and specific response to this customer in 50 words\n"
    
    response1 = getGPTResponse(init_text1 + '""" ' + comment + ' """')
    response2 = getGPTResponse(init_text2 + '""" ' + comment + ' """')
    response3 = getGPTResponse(init_text3 + '""" ' + comment + ' """')
    
    return [response1, response2, response3]

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/review/get", methods=['GET'])
def get_reviews():
    reviews = list(mongo.db.reviews.find({}))
    response = {
        "reviews": reviews,
    }

    return jsonify(json_util.dumps(response))

@app.route("/review/add", methods=['POST'])
def add_review():
    data = request.get_json(silent=True)
    try:
        title = data['title']
        comment = data['comment'][:250]
        name = data['name']
        rating = data['rating']
        date = data['date']
        category = data['category']

        summary = get_summary(comment)

        try:
            posRes = summary[0]
        except:
            posRes = ""
        try:
            negRes = summary[1]
        except:
            negRes = ""
        try:
            reply = summary[2]
        except:
            reply = ""

        review_doc = { 
            'title' : title, 
            'comment' : comment, 
            'rating' : rating,
            'name' : name,
            'date' : date,
            'category' : category,
            'posRes' : posRes,
            'negRes' : negRes,
            'reply' : reply,
        }

        db.reviews.insert_one(review_doc)
        
        return jsonify(json_util.dumps({"message": "success", "data": review_doc})), 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400

@app.route("/reviews/add", methods=['POST'])
def add_reviews():
    multiple_data = request.get_json(silent=True)['reviews']
    c = 0
    for data in multiple_data:
        c += 1
        # print(c)
        try:
            title = data['title']
            comment = data['comment'][:250]
            name = data['name']
            rating = data['rating']
            date = data['date']
            category = data['category']

            summary = get_summary(comment)

            try:
                posRes = summary[0]
            except:
                posRes = ""
            try:
                negRes = summary[1]
            except:
                negRes = ""
            try:
                reply = summary[2]
            except:
                reply = ""

            review_doc = { 
                'title' : title, 
                'comment' : comment, 
                'rating' : rating,
                'name' : name,
                'date' : date,
                'category' : category,
                'posRes' : posRes,
                'negRes' : negRes,
                'reply' : reply,
            }

            db.reviews.insert_one(review_doc)
        except Exception as e:
            print(e)
    
            
    return jsonify(json_util.dumps({"message": "success"})), 200


def create_app():
   return app