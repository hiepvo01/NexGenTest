from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

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
    app.run()