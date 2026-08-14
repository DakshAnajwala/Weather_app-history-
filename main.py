from geopy.geocoders import Nominatim
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily


# def grapher()

def date(year):
    start = datetime(year, 1, 1)
    end = datetime(year, 12, 31)
    return start, end


def latitude_longitute(area):
    loc = Nominatim(user_agent="GeoLoc")
    l_and_l = loc.geocode(area)
    print(l_and_l)
    print(f"The latitude for {area} is {l_and_l.latitude}")
    print(f"The longitude for {area} is {l_and_l.longitude}")
    return l_and_l.latitude, l_and_l.longitude


if __name__ == "__main__":
    place = input("Enter your desired city for latitude and longitude ")
    print(latitude_longitute(area=place))
    lat_long = latitude_longitute(area=place)
    dt_yr = (input("Enter the year of which weather data is needed(default is 2021) "))
    if not dt_yr:
        dt_yr = '2021'
    dt_yr = int(dt_yr)
    date_yr = date(dt_yr)
    area = Point(lat=lat_long[0], lon=lat_long[1])

    data = Daily(area, date_yr[0], date_yr[1])
    data = data.fetch()
    data.plot(y=['tavg', 'prcp', 'wdir', "wspd", "pres"], subplots=True, layout=(3, 2))
    plt.show()
