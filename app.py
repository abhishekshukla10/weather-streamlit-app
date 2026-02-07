import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

weather_api_key=os.getenv("WEATHER_API_KEY")



st.title("🌤️ Weather App")

city = st.text_input("Enter city name")

if city:
    
    url = "https://api.weatherapi.com/v1/current.json" 

    params = { 

    "key": weather_api_key, 

    "q": city

    } 
     # Use the get function from the requests library to store the response from the API 

    response = requests.get(url, params=params)
    
    if response.status_code ==200:

        data=response.json()

        # Extract the values
        temp_c = data['current']['temp_c']
        wind_kph = data['current']['wind_kph']


        st.success(f"📍 City: {city}")
        st.write(f"Temperature: {temp_c}°C")
        st.write(f"Wind Speed: {wind_kph} kph")

    else:
        st.error("City not found ❌") 

