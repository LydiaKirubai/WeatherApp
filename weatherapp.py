import requests

API_KEY = 'da2ff59b0b6e2cc401ba41f911b96fcc'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity: {data['main']['humidity']} %")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print(f"Error {response.status_code}: {response.json().get('message')}")

# Example
city = input("Enter city: ")
get_weather(city)
