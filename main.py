import tkinter as tk
import requests
# Replace with your OpenWeatherMap API key
api_key = "your Api key here"

def get_weather_data(location):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code}")
    return None

def display_weather(data):
  if data:
    city = data["name"]
    temperature = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    weather_label.config(text=f"\nWeather in {city}:\n  Temperature: {temperature:.2f} °C\n  Humidity: {humidity}%\n  Description: {description}")
  else:
    weather_label.config(text="Error: Unable to retrieve weather data.")

def get_weather():
  location = location_entry.get()
  weather_data = get_weather_data(location)
  display_weather(weather_data)

root = tk.Tk()
root.title("Weather App")

# Set background image
bg_image = tk.PhotoImage(file="Untitled design.png")  # Replace with your image path
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Input field for location
location_label = tk.Label(root, text="Enter city or ZIP code:")
location_label.pack()
location_entry = tk.Entry(root, font=("Arial", 14), foreground="black",bg="lightgray", borderwidth=2)
location_entry.pack()

# Button to trigger weather retrieval
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Label to display weather information
weather_label = tk.Label(root, text="")
weather_label.pack()

root.mainloop()
