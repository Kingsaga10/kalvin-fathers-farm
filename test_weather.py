import requests

api_key = "actual withheld"
city = "Wa,gh"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()
print(data)