from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir + 'clothes.db')

@app.route('/')
def hello_world():
    return jsonify(message="Hello World"), 200

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message= "Sorry " + name + ", You are not old enough")
    else:
        return jsonify(message= name + ", You are old enough")
    
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message= "Sorry " + name + ", You are not old enough")
    else:
        return jsonify(message= name + ", You are old enough")
    
if __name__ == '__main__':
    app.run()