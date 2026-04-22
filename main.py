import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)
data = response.json()

temp = data["current_condition"][0]["temp_C"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]
humidity = data["current_condition"][0]["humidity"]

print(f"\nWeather in {city}:")
print(f"Temperature: {temp}°C")
print(f"Condition: {weather}")
print(f"Humidity: {humidity}%")
print(f"Feels Like: {data['current_condition'][0]['FeelsLikeC']}°C")
print(f"Wind Speed: {data['current_condition'][0]['windspeedKmph']} km/h")
