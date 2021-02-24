from flask import Flask,redirect, url_for,render_template,request
import os
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast


secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True

# Defining the home page of our site
@app.route("/",methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("test1.html")
    else:
        # pass # unknown
        return render_template("index.html")

@app.route("/data_display" , methods=['GET', 'POST'])
def run_script():
    
     data = pd.read_csv('C:\\Users\\test1\\source\\repos\\raonarendra\\monitoring system\\templates\\users.csv')  # read CSV
     data = data.to_dict()  # convert dataframe to dictionary
     return {'data': data}, 200  # return data and 200 OK code
     

if __name__ == "__main__":
    app.run()
    
