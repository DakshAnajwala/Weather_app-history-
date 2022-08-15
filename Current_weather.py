import requests
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Normals

def weather_part_a(city):

    print(city)

    print('Weather Report for:'+ city)

    url = 'https://wttr.in/{}'.format (city)
    resource = requests.get(url)

    print(resource.text)

def graph(city,start_date,end_date):
    data =


if __name__ == "__main__":
    area = input("Enter you desired area: ")
    print(weather_part_a(city=area))
    
