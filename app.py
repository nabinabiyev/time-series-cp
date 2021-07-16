from flask import Flask, jsonify, request
from flask import render_template, send_from_directory
from model import train_and_predict
import os

if not os.path.exists("graph.png"):
    train_and_predict()

app=Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
