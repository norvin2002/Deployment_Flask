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
@app.route("/predict")
def predict():
    return "The API works"

app.run()
