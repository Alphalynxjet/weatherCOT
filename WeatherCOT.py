import requests
from datetime import datetime, timedelta
import socket

# Define the coordinates and location name
latitude = 56.95
longitude = 24.11
location_name = "Riga"

# Define the transport protocol (TCP or UDP)
transport_protocol = "TCP"  # Change to "UDP" if desired

# Define the server IP address and port
server_ip = "127.0.0.1"
server_port = 9101

# API request URL
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,snow_depth,cloudcover,windspeed_10m,winddirection_10m&current_weather=true&windspeed_unit=ms&forecast_days=1"

# Send the API request
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract hourly weather data
hourly_data = data["hourly"]

# Get the current time
current_time = datetime.now()

# Find the nearest time in the hourly data
hourly_times = [datetime.fromisoformat(time) for time in hourly_data["time"]]
nearest_time = min(hourly_times, key=lambda time: abs(time - current_time))

# Find the index of the nearest time in the hourly data
hour_index = hourly_times.index(nearest_time)

# Extract hourly weather information for the nearest time
temperature_2m = hourly_data["temperature_2m"][hour_index]
relativehumidity_2m = hourly_data["relativehumidity_2m"][hour_index]
dewpoint_2m = hourly_data["dewpoint_2m"][hour_index]
apparent_temperature = hourly_data["apparent_temperature"][hour_index]
precipitation_probability = hourly_data["precipitation_probability"][hour_index]
precipitation = hourly_data["precipitation"][hour_index]
rain = hourly_data["rain"][hour_index]
showers = hourly_data["showers"][hour_index]
snowfall = hourly_data["snowfall"][hour_index]
snow_depth = hourly_data["snow_depth"][hour_index]
cloudcover = hourly_data["cloudcover"][hour_index]
windspeed_10m = hourly_data["windspeed_10m"][hour_index]
winddirection_10m = hourly_data["winddirection_10m"][hour_index]

# Format the CoT message string
cot_message = """<?xml version="1.0" encoding="UTF-8"?>
<event version="2.0" uid="{0}" type="a-u-G-E-S" how="m-g" time="{1}" start="{2}" stale="{3}">
    <point lat="{4}" lon="{5}" hae="0.0" ce="9999999.0" le="9999999.0"/>
    <detail>
        <contact callsign="{6} METEO"/>
        <remarks>Temperature: {7:.1f}\u00b0C, Relative Humidity: {8}%, Dew Point: {9:.1f}\u00b0C, Apparent Temperature: {10:.1f}\u00b0C, Precipitation Probability: {11}%, Precipitation: {12}mm, Rain: {13}mm, Showers: {14}mm, Snowfall: {15}cm, Snow Depth: {16}cm, Cloud Cover: {17}%, Wind Speed: {18}m/s, Wind Direction: {19}\u00b0</remarks>
        <track course="{19}" speed="{18}"/>
        <source type="dataFeed" name="NODE-RED" uid="node-red-123456789"/>
    </detail>
</event>""".format(
    location_name,
    current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    (current_time + timedelta(minutes=20)).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    latitude,
    longitude,
    location_name,
    temperature_2m,
    relativehumidity_2m,
    dewpoint_2m,
    apparent_temperature,
    precipitation_probability,
    precipitation,
    rain,
    showers,
    snowfall,
    snow_depth,
    cloudcover,
    windspeed_10m,
    winddirection_10m
)

# Print the sent CoT
print("Sent CoT:")
print(cot_message)

# Send the CoT message via TCP or UDP
if transport_protocol == "TCP":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))
    sock.sendall(cot_message.encode())
    sock.close()
elif transport_protocol == "UDP":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(cot_message.encode(), (server_ip, server_port))
    sock.close()
else:
    print("Invalid transport protocol specified. Please choose TCP or UDP.")
