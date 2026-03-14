import numpy as np
from flask import Flask , render_template, request
import joblib
from utilities import predict_input
import os


titanic = joblib.load('models/Titanic.joblib')
scaler = titanic['scaler']
encoder = titanic['encoder']
imputer = titanic['imputer']
model = titanic['model']
input_cols = titanic['input_cols']
numeric_cols = titanic['numeric_cols']
categorical_cols = titanic['categorical_cols']


app = Flask(__name__)

@app.route('/', methods= ["GET", "POST"])
def home() : 
        return render_template('index.html')


@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        age = request.form.get('age')
        cabin = request.form.get('cabin')
        Embarked = request.form.get('Embarked')
        sex = request.form.get('sex')
        SibSp = request.form.get('SibSp')
        Parch = request.form.get('Parch')
        Fare = request.form.get('Fare')
        Pclass = request.form.get('pclass')
        Name = request.form.get('name')
        
    
        inputs = {
        'Pclass': Pclass,
        'Sex': sex,
        'Age': age,
        'SibSp': SibSp,
        'Parch': Parch,
        'Fare': Fare,
        'Embarked': Embarked,
        'Cabin': cabin,
        'Name': Name}

        print(age)

        prediction, probs = predict_input(inputs, imputer, scaler, numeric_cols, encoder, categorical_cols, model)

        if prediction == 1:
             prediction ='Survived'
        else:
             prediction = "Didn't Survive"
        predicted = True
        print(prediction)
        return render_template("index.html", prediction = [prediction, probs], predicted=predicted)

    

if __name__  == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host = "0.0.0.0", port= port)
