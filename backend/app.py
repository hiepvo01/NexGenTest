from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from flask_marshmallow import Marshmallow
import pickle
import os
import numpy as np
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'gloves.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

""" App Routes """

@app.route('/')
def hello_world():
    return jsonify(message="Hello this is NexGenGlove API"), 200

@app.route('/all_data', methods=['GET'])
def all_data():
    cases_list = Case.query.all()
    result = cases_schema.dump(cases_list)
    return jsonify(result)

@app.route('/predict', methods=['POST'])
def predict(): 
    air_temp = int(request.json['air_temp'])
    humidity = int(request.json['humidity'])
    wind_speed = int(request.json['wind_speed'])
    active = int(request.json['active'])
    hours = int(request.json['hours'])
    glove = int(request.json['glove'])
    gloves = [0.5, 1.3, 2.0, 2.4]
    clo = gloves[int(glove)]
    
    print(air_temp)
    
    model1 = pickle.load(open('trained/dexterity.pkl', 'rb'))
    model2 = pickle.load(open('trained/frostbite.pkl', 'rb'))
    
    dexterity = model1.predict(np.array([[air_temp, humidity, wind_speed, active, hours, clo]]))
    frostbite = model2.predict(np.array([[air_temp, humidity, wind_speed, active, hours, clo]]))
    
    return jsonify(dexterity=dexterity[0], frostbite=frostbite[0])
    
# @app.route('/url_variables/<string:name>/<int:age>')
# def url_variables(name: str, age: int):
#     if age < 18:
#         return jsonify(message= "Sorry " + name + ", You are not old enough")
#     else:
#         return jsonify(message= name + ", You are old enough")
    
    
""" Database Config """

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Databases created')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Databases dropped')

"""Database Models"""

class Case(db.Model):
    __tablename__ = 'cases'
    index = Column(Integer, primary_key = True)
    air_temp = Column(Integer)
    humidity = Column(Integer)
    wind_speed = Column(Integer)
    active = Column(Integer)
    hours = Column(Integer)
    clo = Column(Float)
    dexterity = Column(Float)
    frostbite = Column(Float)

class CaseSchema(ma.Schema):
    class Meta:
        fields = ('index', 'air_temp', 'humidity', 'wind_speed', 'active', 'hours', 'clo', 'upper', 'dexterity', 'frostbite')

case_schema = CaseSchema()
cases_schema = CaseSchema(many=True)

    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)