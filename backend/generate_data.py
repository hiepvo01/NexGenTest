import pandas as pd
import sqlite3 as sql
import random
from sklearn import linear_model
import pickle

air_temp = []
humidity = []
wind_speed = []
active = []
hours = []
clo = []
dexterity = []
frostbite = []
gloves = [0.5, 1.3, 2.0, 2.4]

for i in range(500):
    air_temp.append(random.randint(-20, 40))
    humidity.append(random.randint(15, 75))
    wind_speed.append(random.randint(1, 6))
    active.append(random.randint(0, 1))
    hours.append(random.randint(0, 20))
    clo.append(random.choice(gloves))

    dexterity.append(random.uniform(0, 10))
    frostbite.append(random.uniform(0, 10))
    
df = pd.DataFrame(list(zip(air_temp, humidity, wind_speed, active, hours, clo, dexterity, frostbite)),
               columns =['air_temp', 'humidity', 'wind_speed', 'active', 'hours', 'clo', 'dexterity', 'frostbite'])

# Train linear regression models
X = df.drop(['dexterity', 'frostbite'], axis=1)
Y1 = df['dexterity']
Y2 = df['frostbite']
regr1 = linear_model.LinearRegression()
regr1.fit(X, Y1)
regr2 = linear_model.LinearRegression()
regr2.fit(X, Y2)

# Save trained models
filename = 'trained/dexterity.pkl'
pickle.dump(regr1, open(filename, 'wb'))
filename = 'trained/frostbite.pkl'
pickle.dump(regr2, open(filename, 'wb'))

# Save data to sqlite database
conn = sql.connect('gloves.db')
df.to_sql('cases', conn)