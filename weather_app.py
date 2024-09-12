import requests
from api_key import api_key

def fetch_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == 200:
        city_name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
    else:
        print("City not found. Please enter a valid city name.")

def main():
    city_name = input("Enter city name: ")
    weather_data = fetch_weather(city_name)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
