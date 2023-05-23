# WeatherCOT

![WeatherCOT Example](https://raw.githubusercontent.com/Alphalynxjet/weatherCOT/main/weathercot.png)

WeatherCOT is a Python script that retrieves current weather information from the Open-Meteo API and sends it as a Cursor-On-Target (CoT) message over TCP. This script can be useful for integrating real-time weather data into CoT-enabled systems or applications. 

## Features

- Retrieves current weather data for a specific location using latitude and longitude coordinates.
- Wind direction is shown using course arrow in ATAK
- Sends the weather information as a CoT message over TCP.
- Customizable location, API coordinates, and TCP server settings.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3
- Requests library (install using `pip install requests`)

## Usage

1. Clone the repository or download the `WeatherCOT` script.

2. Open the `WeatherCOT.py` file in a text editor.

3. Set the following parameters at the top of the script:

   - `latitude`: The latitude coordinate of the location for which you want to retrieve the weather information.
   - `longitude`: The longitude coordinate of the location.
   - `location_name`: The name of the location (used in the CoT message).
   - `server_ip`: The IP address of the COT server ( TCP ONLY )
   - `server_port`: The port number of the COT server ( TCP ONLY )

4. Save the changes to the script.

5. Open a terminal or command prompt and navigate to the directory where the `WeatherCOT.py` file is located.

6. Run the script using the following command:

python3 WeatherCOT.py

7. The script will retrieve the current weather data, format it into a CoT message, and send it over TCP to the specified server. The sent CoT message will be printed in the console.

8. You can integrate this script into your own applications or systems by modifying the CoT message format or using the retrieved weather data in your desired way.

For Ubuntu the best way to run the script on a repeated timer is using crontab.

## License

This project is licensed under the MIT License. Feel free to modify and distribute it according to your needs.

## Acknowledgments

- This script utilizes the Open-Meteo API to retrieve weather data. Visit their website for more information: [Open-Meteo](https://open-meteo.com/)

- BTW, this whole script and readme.md was made using ChatGPT
