import requests
from datetime import datetime
api_key = '56dfc7287fb67d7962bb58698974956d'
location = input("Enter the City Name : ")
degree_sign = u"\N{DEGREE SIGN}"
 
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
 
temp = ((api_data['main']['temp']) - 273.15)
feels_like = ((api_data['main']['feels_like']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%a, %d %b %Y | %I:%M:%S %p")
 
with open('weather.txt', 'w') as f:
 
    f.write("----------Weather Stats for - {} | {}-----------------\n".format(location.upper(), date_time))
    f.write("Current temperature is    : {:.2f}{} C.\n".format(temp,degree_sign))
    f.write("You Feels Like temperture : {:.2f}{} C.\n".format(feels_like,degree_sign))
    f.write("Current weather desc      : {}.\n".format(weather_desc))
    f.write("Current Humidity          : {} %.\n".format(hmdt))
    f.write("Current wind speed        : {} kmph.\n".format(wind_spd))