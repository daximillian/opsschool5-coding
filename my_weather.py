#!/usr/bin/env python

from requests import get
import json
import sys

def main(weather_args):
    """Print out the weather in Celcius or Farenheit for all cities required. 

	Args:
		weather_args: A list of cities, optionally with a -c (for Celcius) or -f (for Farenheit) flag after the city name.  
	"""
    i = 1
    while i < len(weather_args):
        city = weather_args[i].strip(',')
        if i <= (len(weather_args) - 2):
            if weather_args[i + 1].strip(',') == '-c' or weather_args[i + 1].strip(',') == '-f':
                temp_arg = weather_args[i + 1].strip(',')
                print_city_weather(city, temp_arg)
                i += 1
            else:    
                print_city_weather(city)
        else:
            print_city_weather(city)
        i += 1


def print_city_weather(city_name, temp_opt = '-c'):
    """Print out the weather in Celcius or Farenheit for a specified city. 
    An error is issued for none existent cities.

	Args:
		city_name: A string with a city name.
        temp_opt: -c (for Celcius) or -f (for Farenheit). Default -c.  
	"""
    weather_response = get('http://api.weatherstack.com/current?access_key=6152bde38aaede176593ecb705b6892e&query=' + city_name)
    city_json = json.loads(weather_response.text)

    try:
        city_temp = city_json['current']['temperature']
        temp_scale = 'Celcius' 

        if temp_opt == '-f':
            temp_scale = 'Farenheit'
            city_temp = (city_temp * 1.8) + 32

        print('The weather in {} is {} degrees {}'.format(city_json['location']['name'], str(city_temp), temp_scale))
    except (KeyError) as city_error:
        print('Error: city does not exist. Please try cities like London, New York, Cape Town or Mumbai',file=sys.stderr)
    

if __name__ == '__main__':
    main(sys.argv)
