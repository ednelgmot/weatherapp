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
def index():
    data = fetch_data()
    return render_template('index.html', data=data)

#####

@app.route('/alerts')
def alerts():
    data = fetch_alerts()
    return render_template('alerts.html', data=data)

if __name__ == "__main__":
    app.run(port=8000, debug=True)