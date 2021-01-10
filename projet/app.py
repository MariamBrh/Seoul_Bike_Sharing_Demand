# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 00:05:26 2021

@author: mariam
"""
  
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features = [x for x in request.form.values()]
    
    visibility = request.form.get('Visibility')
    solar = request.form.get("Solar Radiation")
    rainfall = request.form.get("Rainfall")
    snowfall = request.form.get("Snowfall")
    holiday = request.form.get('Holiday')
    seasons = request.form.get('Seasons')
    functioning = request.form.get('Functioning')
    month = request.form.get('Month')
    weekday = request.form.get('Weekday')
    
    
    # Encoding the categorical features
    if(float(visibility) <= 500):
        features[4] = str(1)
    elif(float(visibility) <= 1000):
        features[4] = str(2)
    elif(float(visibility) <= 1500):
        features[4] = str(3)
    else:
        features[4] = str(4)
        
    if(float(solar) > 0):
        features[5] = str(1)
    else:
        features[5] = str(0)
        
    if(float(rainfall) > 0):
        features[6] = str(1)
    else:
        features[6] = str(0)
    
    if(float(snowfall) > 0):
        features[7] = str(1)
    else:
        features[7] = str(0)
        
    if(holiday.lower == "no holiday"):
        features[9] = str(0)
    else:
        features[9] = str(1)
    
    if(seasons == "Winter"):
        features[8] = str(1)
    elif(seasons == "Spring"):
        features[8] = str(2)
    elif(seasons == "Summer"):
        features[8] = str(3)
    elif(seasons == "Autumn"):
        features[8] = str(4)

    if(functioning.lower == "no"):
        features[10] = str(0)
    else:
        features[10] = str(1)
    
    
    if ((features[4]==str(4) or features[4]==str(3)) and features[6]==str(0) and features[7]==str(0)):
        features.append(str(1))
    elif ((features[4]==str(1) or features[4]==str(2))  and features[6]==str(0) and features[7]==str(0)):
        features.append(str(2))
    elif ((features[6]==str(0) and features[7]==str(1)) or (features[6]==str(1) and features[7]==str(0))):
        features.append(str(3))
    else:
        features.append(str(4))
    
    if(month == "January"):
        features[11] = str(1)
    elif(month == "February"):
        features[11] = str(2)
    elif(month == "March"):
        features[11] = str(3)
    elif(month == "April"):
        features[11] = str(4)
    elif(month == "May"):
        features[11] = str(5)
    elif(month == "June"):
        features[11] = str(6)
    elif(month == "July"):
        features[11] = str(7)
    elif(month == "August"):
        features[11] = str(8)
    elif(month == "September"):
        features[11] = str(9)
    elif(month == "October"):
        features[11] = str(10)
    elif(month == "November"):
        features[11] = str(11)
    else:
        features[11] = str(12)
    
    
    if(weekday == "Monday"):
        features[14] = str(1)
    elif(weekday == "Tuesday"):
        features[14] = str(2)
    elif(weekday == "Wednesday"):
        features[14] = str(3)
    elif(weekday == "Thursday"):
        features[14] = str(4)
    elif(weekday == "Friday"):
        features[14] = str(5)
    elif(weekday == "Saturday"):
        features[14] = str(6)
    else:
        features[14] = str(7)
    
    
    final_features = np.array([features])
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Number of Rented Bikes should be {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict(np.array(list(data.values())))

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
