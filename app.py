# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:11:36 2022

@author: avdhu
"""

import flask
from flask import Flask,request,jsonify,render_template
import pandas as pd
import numpy as np
import pickle
app = Flask(__name__)
filename = "MGA.pkl"
model = pickle.load(open(filename,"rb"))
@app.route('/')
def hp():
    return render_template('homepage.html')

@app.route('/predict',methods = ["POST"])
def up():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    arr = np.array([[data1,data2,data3]])
    pred = model.predict(arr)
    return render_template("nextpage.html",)

if __name__ == "main":
    app.run(debug=True)