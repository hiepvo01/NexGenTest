from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'clothes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

""" App Routes """

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
    
    
""" Database Config """

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Databases created')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Databases dropped')

@app.cli.command('db_seed')
def db_seed():
    case1 = Case( id=1,
                air_temp = -11,
                humidity = 75,
                wind_speed = 2,
                active = 116,
                rest = 0,
                head = 'cap',
                upper = 'armor',
                hands = 'thin gloves',
                legs = 'shorts',
                feet = 'boots')

    case2 = Case( id=2,
                air_temp = 12,
                humidity = 60,
                wind_speed = 3,
                active = 0,
                rest = 90,
                head = '',
                upper = 'shirt',
                hands = '',
                legs = 'jeans',
                feet = 'sneakers')
    
    case3 = Case( id=3,
                air_temp = -5,
                humidity = 50,
                wind_speed = 1,
                active = 220,
                rest = 0,
                head = 'beanie',
                upper = 'hoodie',
                hands = 'gloves',
                legs = 'jeans',
                feet = 'slippers')
    
    case4 = Case( id=4,
                air_temp = 15,
                humidity = 65,
                wind_speed = 4,
                active = 22,
                rest = 0,
                head = 'beanie',
                upper = 'jacket',
                hands = '',
                legs = 'shorts',
                feet = 'socks')

    db.session.add(case1)
    db.session.add(case2)
    db.session.add(case3)
    db.session.add(case4)
    
    db.session.commit()
    print('Databases seeded')

"""Database Models"""

class Case(db.Model):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key = True)
    air_temp = Column(Integer)
    humidity = Column(Integer)
    wind_speed = Column(Integer)
    active = Column(Integer)
    rest = Column(Integer)
    head = Column(String)
    upper = Column(String)
    hands = Column(String)
    legs = Column(String)
    feet = Column(String)

class CaseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'air_temp', 'humidity', 'wind_speed', 'active', 'rest', 'head', 'upper', 'hands', 'legs', 'feet')

case_schema = CaseSchema()
cases_schema = CaseSchema(many=True)

    
if __name__ == '__main__':
    app.run()