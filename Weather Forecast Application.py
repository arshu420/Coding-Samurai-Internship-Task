"""To use this code, you'll need to sign up for a free API key from OpenWeatherMap 
(https://openweathermap.org/api) and replace "YOUR_API_KEY" with your actual API key in the code."""

import requests

# OpenWeatherMap API key (replace with your own)
API_KEY = "YOUR_API_KEY"

def get_weather_data(city_name, unit="metric"):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&units={unit}&appid={API_KEY}"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_weather_info(data, unit):
    if data is not None:
        print("\nWeather Information for", data["name"], ",", data["sys"]["country"])
        print("Temperature:", data["main"]["temp"], f"°{unit}")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
        print("Weather Conditions:", data["weather"][0]["description"])
    else:
        print("Weather data not found. Please check the city name or try again later.")

def main():
    print("Welcome to the Weather Forecast Application!")
    city_name = input("Enter the name of the city or location: ")
    unit = input("Choose temperature units (Celsius or Fahrenheit): ").lower()

    if unit not in ["celsius", "fahrenheit"]:
        print("Invalid choice. Defaulting to Celsius.")
        unit = "celsius"

    data = get_weather_data(city_name, unit)

    display_weather_info(data, unit)

if __name__ == "__main__":
    main()
