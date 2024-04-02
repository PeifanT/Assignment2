import requests

def get_coordinates(city_name, api_key):
    """Fetch latitude and longitude for a city name using the Geocoding API."""
    geo_base_url = "http://api.openweathermap.org/geo/1.0/direct"
    geo_params = {
        "q": city_name,
        "limit": 1,
        "appid": api_key
    }
    response = requests.get(geo_base_url, params=geo_params)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
    return None, None

def get_weather_forecast(latitude, longitude, api_key):
    """Fetch the weather forecast using geographical coordinates."""
    forecast_base_url = "http://api.openweathermap.org/data/2.5/forecast"
    forecast_params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(forecast_base_url, params=forecast_params)
    if response.status_code == 200:
        return response.json()
    return {}

# Main program
api_key = "4f68113019b01d458e342f56b282b531"
city_name = "Revere"

latitude, longitude = get_coordinates(city_name, api_key)
if latitude is not None and longitude is not None:
    forecast = get_weather_forecast(latitude, longitude, api_key)
    if forecast:
        # Print weather forecast for the next 24 hours (8 intervals of 3 hours each)
        print(f"Weather forecast for {city_name} for the next 24 hours:")
        for entry in forecast['list'][:10]:  # Adjust the slice as needed
            weather_summary = {
                "temperature": entry['main']['temp'],
                "feels_like": entry['main']['feels_like'],
                "description": entry['weather'][0]['description'],
                "time": entry['dt_txt']
            }
            print(f"Time: {weather_summary['time']}, Temp: {weather_summary['temperature']}°C, "
                  f"Feels like: {weather_summary['feels_like']}°C, Description: {weather_summary['description']}")
    else:
        print("Unable to retrieve weather data.")
else:
    print("Unable to retrieve coordinates for the city.")



