from flask import Flask, request
import json
import pandas as pd
import joblib

app = Flask(__name__)
forest = joblib.load("forest_v1.joblib")

@app.route("/")
def index():
    return "Hello world!"

# this is our API endpoint
# this is actually a get endpoint where user can deliver payload information to
@app.route("/predict", methods = ['GET'])
def predict():
    # take the API payload as JSON format
    json_ = request.json
    df = pd.read_json(json_)

    prediction = forest.predict(df)

    # turn the prediction from np array into a proper list
    # pack the list into a dictionary

    return {"prediction" : list(prediction)}

#app.run() -- if running from local microserver

# if deployed to Heroku:
if __name__ == '__main__':
    app.run()

