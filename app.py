def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # For Celsius
    }
    response = requests.get(base_url, params=params)
    
    # Check for debugging purposes:
    st.write(response.status_code)  # Print status code
    st.write(response.json())  # Print the actual API response content

    if response.status_code == 200:
        return response.json()
    else:
        return None
