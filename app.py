#  Name:    flask.weatherapp
#  Author:  Thomas Glende
#  Init:    June 11, 2024
#  Purpose: Flask web app to output weather info from API calls
#
# type exit to get out of the virtual env
#
from flask import Flask, render_template, url_for, request
from datetime import datetime
import logging
import requests
import sys
from datapull import fetch_data, fetch_alerts

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

#####

@app.route('/alerts')
def alerts():
    data = fetch_alerts()
    return render_template('alerts.html', data=data)

@app.route('/forecast', methods=['POST'])
def forecast():
    data = fetch_data()
    return render_template('forecast.html', data=data)

#####
if __name__ == "__main__":
    app.run(port=8000, debug=True)