import json

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    # extract values from the event object we got from the Lambda service and store in a variable
    city_name = event['cityName']

    # for AWS requests is set as a layer
    import requests

    # could be set with AWS Secrets Manager
    API_key = 'secret'
    CITY_API = 'https://api.openweathermap.org/data/2.5/weather'

    # params set is provided by api.openweathermap.org
    params = {
        'q': city_name,
        'units': 'metric',
        'appid': API_key
    }

    response = requests.get(f"{CITY_API}", params=params)

    if response.status_code == 200:
        res = response.json()
        temp = res['main']['temp']
        conditions = res['weather'][0]['main']
        wind = res['wind']['speed']
        pressure = res['main']['pressure']
        humidity = res['main']['humidity']
        resp = {}
        resp = {
            'Temprature': temp,
            'Weather conditions': conditions,
            'Wind': wind,
            'Wind dir': '',
            'Pressure': pressure,
            'Humidity': humidity
        }
    # return a properly formatted JSON object
        return {
        'statusCode': 200,
        'body': json.dumps('Got the city ' + resp)
        }
    return {
        # returns 200 for the lambla anyway
        'statusCode': 200,
        'body': json.dumps("can't find this city!")
    }
