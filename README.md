# Seoul_Bike_Sharing_Demand
***Python for Data Analaysis***

![alt text](https://github.com/MariamBrh/Seoul_Bike_Sharing_Demand/blob/main/img/thumbnail_VELO.png)

Seoul is a city spread over more than 600 km2, six times the size of Paris. It is necessary to take precautions when it comes to traveling, especially at peak hours, which generate end less traffic jams in the city's streets.

Paris has its "vélib'" and, for a few years now, Seoul has its equivalent the "Ddareungi". Bicycles, which were not very visible until a few years ago, are now widely used in the South Korean capital and even in other provincial cities.

In this report we will study the bicycle **rental data** in Seoul for the year 2018. The objective of our analysis is to discover the factor(s) that determine the demand for self-service bicycle rentals, build statistical models and then try to make rental prediction based on the information and models available to us. Our data mining and analysis will be done in Python.

/!\ Please note that scrolling in the API is not possible, so please use the "Tab" keypad to input your values. The prediction will be displayed at the end of the page, use the "Tab" keypad to see it.

## Data Information
- Date: day-month-year format
- Rented Bike count: Count of bikes rented at each hour (target)
- Hour: Hour of the day
- Temperature - Celsius
- Humidity - %
- Windspeed - m/s
- Visibility - 10m
- Dew point temperature - Celsius
- Solar radiation - MJ/m2
- Rainfall - mm
- Snowfall - cm
- Seasons - Winter, Spring, Summer, Autumn
- Holiday - Holiday/No holiday
- Functional Day - No(Non Functional Hours)/Yes(Functional hours)

## Step of the Prediciton:  
- Data Cleaning
- Data Visualization
- Data Pre-Processing
- Modelling
- Api
  
 
## The repositery contains:
* The Jupyter Notebook file
* Slides of the report of the analysis
* The Realease of the model within an API 
<br> 

## Conclusion :
Through the exploration of this dataset and the analysis performed on it we discovered that time of day and temperature are the two most important factors that determine the demand for bicycle rental in Seoul.

Using Xgboost , a well advanced scientific tool, we were able to predict the number of bikes with a relatively high accuracy. We could try several other models to perhaps build better statistical models that more accurately explain the variations caused by different variables.

## API looks like

![alt text](https://github.com/MariamBrh/Seoul_Bike_Sharing_Demand/blob/main/img/api.PNG)
