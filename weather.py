#!/usr/bin/env python

import click
from requests import get
import json
import sys


@click.command()
@click.option('--token', help='your API token')
@click.option('--city', help='the cities to list')
@click.option('--T', 'temp_scale', type=click.Choice(['Celsius', 'Fahrenheit']), default='Celsius',
              help='temperature scale')
def weather(token, city, temp_scale):
    """This script prints the current temperature in CITY."""
    if temp_scale == 'Fahrenheit':
        temp_unit = 'f'
    else:
        temp_unit = 'm'
    city_list = city.split(',')
    for city in city_list:
        weather_response = get('http://api.weatherstack.com/current?access_key={}&query={}&units={}'.format(token, city,
                                                                                                            temp_unit))
        city_json = json.loads(weather_response.text)
        try:
            city_temp = city_json['current']['temperature']
            print('The weather in {} is {} degrees {}'.format(city_json['location']['name'], str(city_temp),
                                                              temp_scale))
        except KeyError:
            if city_json['error']['code'] == 101:
                print('Error: {} - {}'.format(city_json['error']['type'], city_json['error']['info'], file=sys.stderr))
            else:
                print('Error: city does not exist. Please try cities like London, New York, Cape Town or Blabla',
                      file=sys.stderr)


if __name__ == '__main__':
    weather()