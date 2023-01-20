#Importing essential libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Creating flask app
app = Flask(__name__)

# Loading the pickle model
model = pickle.load(open("model.pkl", "rb"))

# Defining the homepage
@app.route("/")
def Home():
    return render_template("index.html")

# Defining the prediction page
@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = "The flower specie is {}".format(prediction))

# Defining the function to be run first
if __name__=="__main__":
 app.run(debug=True)