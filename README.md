# **Weather App**

## Overview

The Weather App is a Python application that allows users to fetch the current weather for any city using the OpenWeatherMap API. The app returns temperature, a brief description of the weather, and handles errors if the city is not found.

## Features

- Fetches current weather data by city name.
- Displays temperature and weather description.
- Handles errors (e.g., invalid city names).

## Prerequisites

Before running the Weather App, make sure you have the following installed on your system:

- Python 3.6 or higher
- pip (Python package manager)

## Cloning the Repository

To clone this repository to your local machine, follow these steps:

1. Open a terminal or command prompt.
2. Run the following command to clone the repository:

git clone <https://github.com/your-username/weather-app.git>

1. Navigate to the cloned repository:

cd weather-app

## Folder Structure

After cloning, your project folder should look like this:

weather-app/

│

├── weather_app.py # Main Python script

├── api_key.py # File that stores your API key

└── README.md # Project documentation

## Setting Up the API Key

1. **Get an API key** from OpenWeatherMap by signing up and generating a key.
2. Open the api_key.py file and replace the placeholder with your own API key:

api_key = "your_openweathermap_api_key"

## Installing Dependencies

The Weather App uses the requests library to interact with the OpenWeatherMap API. To install this dependency, run:

pip install requests

## Running the Application

1. Once you have set up the API key and installed the dependencies, you can run the application by executing the following command in your terminal:

python weather_app.py

1. The app will prompt you to enter the name of a city. For example:

Enter city name: London

The app will display the weather data, including the temperature in Celsius and a brief weather description:

Weather in London:

Temperature: 15°C

Description: Clouds

## Conclusion

The Weather App is a simple, command-line-based application that fetches current weather data from the OpenWeatherMap API. It’s designed to be easy to set up and use, with room for future enhancements.