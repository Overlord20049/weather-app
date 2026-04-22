import requests

API_KEY = "a63c0ea3b8bf482fbf441845262204"

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print("❌ City not found")
        return

    temp = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    condition = data["current"]["condition"]["text"]

    print(f"\n🌍 City: {city}")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️ Condition: {condition}")

def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
