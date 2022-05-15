import arrow
import requests
from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

start = arrow.now().floor('day')
end = arrow.now().shift(days=1).floor('day')

# response_1 = requests.get(
#   'https://api.stormglass.io/v2/tide/extremes/point',
#   params={
#     'lat': 47.6507,
#     'lng': 52.6962,
#     'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
#     'end': end.to('UTC').timestamp(),  # Convert to UTC timestam
#   },
#   headers={
#     'Authorization': 'd96ae486-d3ac-11ec-88f0-0242ac130002-d96ae4fe-d3ac-11ec-88f0-0242ac130002'
#   }
# )

# json_data_1 = response_1.json()
# json_data_1 = {
#   "data": [
#     {
#       "height": 0.05495762690713992, 
#       "time": "2022-05-14T05:35:00+00:00", 
#       "type": "high"
#     }, 
#     {
#       "height": -0.05629262762378331, 
#       "time": "2022-05-14T12:14:00+00:00", 
#       "type": "low"
#     }, 
#     {
#       "height": 0.035008241192922125, 
#       "time": "2022-05-14T18:28:00+00:00", 
#       "type": "high"
#     }, 
#     {
#       "height": -0.0292143128655908, 
#       "time": "2022-05-14T23:59:00+00:00", 
#       "type": "low"
#     }
#   ]
# }

# response_2 = requests.get(
#   'https://api.stormglass.io/v2/tide/extremes/point',
#   params={
#     'lat': 47.5424,
#     'lng': 52.9204,
#     'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
#     'end': end.to('UTC').timestamp(),  # Convert to UTC timestam
#   },
#   headers={
#     'Authorization': 'd96ae486-d3ac-11ec-88f0-0242ac130002-d96ae4fe-d3ac-11ec-88f0-0242ac130002'
#   }
# )

# json_data_2 = response_2.json()
json_data_2 = {
  "data": [
    {
      "height": 0.05495762690713992, 
      "time": "2022-05-14T05:35:00+00:00", 
      "type": "low"
    }, 
    {
      "height": 0.05629262762378331, 
      "time": "2022-05-14T12:14:00+00:00", 
      "type": "high"
    }, 
    {
      "height": 0.035008241192922125, 
      "time": "2022-05-14T18:28:00+00:00", 
      "type": "high"
    }, 
    {
      "height": -0.0292143128655908, 
      "time": "2022-05-14T23:59:00+00:00", 
      "type": "low"
    }
  ], 
  "meta": {
    "cost": 1, 
    "dailyQuota": 10, 
    "datum": "MSL", 
    "end": "2022-05-15 02:30", 
    "lat": 47.6507, 
    "lng": 52.6962, 
    "requestCount": 11, 
    "start": "2022-05-14 02:00", 
    "station": {
      "distance": 1059, 
      "lat": 42.167, 
      "lng": 41.683, 
      "name": "poti", 
      "source": "sg"
    }
  }
}

@app.route("/data")
def ocean_0():
    response = {"data": [
    {
      "height": 0.05495762690713992, 
      "time": "2022-05-14T05:35:00+00:00", 
      "type": "high"
    }
  ]}
    return response

@app.route('/1')
def ocean_1():
    response = {"data": [
    {
      "height": 0.05495762690713992, 
      "time": "2022-05-14T05:35:00+00:00", 
      "type": "high"
    }, 
    {
      "height": -0.05629262762378331, 
      "time": "2022-05-14T12:14:00+00:00", 
      "type": "low"
    }, 
    {
      "height": 0.035008241192922125, 
      "time": "2022-05-14T18:28:00+00:00", 
      "type": "high"
    }, 
    {
      "height": -0.0292143128655908, 
      "time": "2022-05-14T23:59:00+00:00", 
      "type": "low"
    }
  ]}
    return response
    # return json_data_1

@app.route('/2')
def ocean_2():
    response = {"data": [
     {
      "height": 0.05495762690713992, 
      "time": "2022-05-14T05:35:00+00:00", 
      "type": "low"
    }, 
    {
      "height": 0.05629262762378331, 
      "time": "2022-05-14T12:14:00+00:00", 
      "type": "high"
    }, 
    {
      "height": 0.035008241192922125, 
      "time": "2022-05-14T18:28:00+00:00", 
      "type": "high"
    }, 
    {
      "height": -0.0292143128655908, 
      "time": "2022-05-14T23:59:00+00:00", 
      "type": "low"
    }
  ]}
    return response
    # return json_data_2


if __name__ == "__main__":
    app.run(debug=True)
