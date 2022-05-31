{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "105546e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b47a8769",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, jsonify, render_template\n",
    "#import jinja2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5c99ddda",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as np\n",
    "import numpy as np\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fbcbb2ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8a1e84dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "filename = 'MODEL_GYM_AP.pkl'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "28087668",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = pickle.load(open(filename,'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "64e19863",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def hp(): #home page \n",
    "    return render_template('homepage.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0a7f4391",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/predict',methods = [\"POST\"])\n",
    "def np(): \n",
    "    data1 = request.form['a']\n",
    "    data2 = request.form['b']\n",
    "    data3 = request.form['c']\n",
    "    arr = np.array([[data1,data2,data3]])\n",
    "    pred = model.predict(arr)\n",
    "    return render_template('nextpage.html',data=pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9f61e5be",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"main\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ffaff0e3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
