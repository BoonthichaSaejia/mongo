from flask import Flask
from pymongo import MongoClient
import json

app=Flask(__name__)

@app.route("/")
def home():
    return "This is my homepage"

@app.route("/hello")
def hello():
    return {"message":"Hello this is my API deployed on heroku"}

@app.route("/news")
def news():
    URI = "mongodb+srv://user1:B6210503667mui@cluster0.aahd4.gcp.mongodb.net/test"
    client = MongoClient(URI, retryWrites=False)
    collection=client.foreignNews.News
    query={}
    cursor=collection.find(query)
    for data_in_cursor in cursor[:]:
        return data_in_cursor

if __name__=="__main__":
    app.run()