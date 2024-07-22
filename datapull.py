import requests

API_URL = 'https://api.weather.gov/gridpoints/GSP/126,77/forecast'
ALERT_URL = 'https://api.weather.gov/alerts?point=35.487362,-80.621735'

#####
# evaluate your location
#####
def get_location():
    ip_address = requests.get('http://api.ipify.org').text
    geo_data = requests.get(f'http://ip-api.com/json/{ip_address}').json()
    vlat = geo_data['lat']
    vlon = geo_data['lon']


#####
# fetches the weather forcast for your area
#####
def fetch_data():
    
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Failed to fetch data from the API'}

#####
# fetches the weather alerts for your area
#####
def fetch_alerts():
    
    response = requests.get(ALERT_URL)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Failed to fetch data from the API'}