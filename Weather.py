import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_info = {
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return None

def main():
    api_key = "4acaa621fce479e912f721b0b9bb8494"  
    location = input("Enter a city or ZIP code: ")
    weather_data = get_weather(api_key, location)
    
    if weather_data:
        print("\nCurrent Weather:")
        for key, value in weather_data.items():
            print(f"{key}: {value}")
    else:
        print("Error: Unable to fetch weather data.")

if __name__ == "__main__":
    main()
