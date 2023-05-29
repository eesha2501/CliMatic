import requests


def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

def kelvin_to_fahrenheit(temp_k):
    return (temp_k - 273.15) * 9/5 + 32

def get_weather(city_name, temp_unit):
    # define the API endpoint
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # enter your unique API key here
    api_key = "54415c153b88c3aa6f295f88c24c6d6a"

    # complete api url
    complete_url = base_url + "?q=" + city_name + "&appid=" + api_key 

    # request the data
    response = requests.get(complete_url)

    # check the response status
    if response.status_code == 200:
        data = response.json()

        # extract relevant data
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']

        # convert temperature to the requested unit
        temp_k = main['temp']
        if temp_unit == 'C':
            temp = kelvin_to_celsius(temp_k)
        elif temp_unit == 'F':
            temp = kelvin_to_fahrenheit(temp_k)
        else:  # default to Kelvin if an unrecognized unit is provided
            temp = temp_k

        # print the results
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temp}{temp_unit}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind speed: {wind['speed']}m/s")
        print(f"Weather description: {weather_desc}")
    else:
        print(f"Error: Unable to fetch weather data for {city_name}")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")

def main():
    city_name = input("Please enter the name of the city: ")
    temp_unit = input("Please enter the temperature unit (K, C, F): ")
    get_weather(city_name, temp_unit)

if __name__ == "__main__":
    main()
