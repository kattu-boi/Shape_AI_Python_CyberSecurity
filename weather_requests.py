import requests
r = requests.get('https://github.com/kattu-boi/Shape_AI_Python_CyberSecurity/blob/main/weather.py')

with open('weather_requests.txt','wb') as fd:
    fd.write(r.content)