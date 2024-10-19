import requests
import streamlit as st
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# Function to get weather data from OpenWeatherMap API
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # For Celsius, use 'metric'. For Fahrenheit, use 'imperial'.
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit app UI
def main():
    st.title("Weather App 🌦️")
    
    # Get the city name from user
    city = st.text_input("Enter the city name")
    
    if st.button("Get Weather"):
        if city:
            weather_data = get_weather(city)
            if weather_data:
                # Extract relevant weather information
                st.write(f"## Weather in {city.capitalize()}")
                st.write(f"**Temperature:** {weather_data['main']['temp']}°C")
                st.write(f"**Weather:** {weather_data['weather'][0]['description'].capitalize()}")
                st.write(f"**Humidity:** {weather_data['main']['humidity']}%")
                st.write(f"**Wind Speed:** {weather_data['wind']['speed']} m/s")
            else:
                st.error("City not found or API limit exceeded!")
        else:
            st.error("Please enter a city name")

if __name__ == "__main__":
    main()
