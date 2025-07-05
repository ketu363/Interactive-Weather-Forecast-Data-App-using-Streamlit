import requests

API_KEY = "747b52f4707b553a60e18bfd4c84e4e7"


def get_data(place, forecast_days=None, kind=None):
    # This url give the city weather data in json for next 5 days in the in tervel of 3 hr
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    # The number of forcast per day is 8  so if we find number for values for 2 day so total forcast will be 8*2=16
    nr_values = 8 * forecast_days
    # getting forcast values from the forcast data
    filtered_data = filtered_data[:nr_values]
    # Filtering data on basis of kind value
    if kind == "Temperature":
        # Filtering the temperature data
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
        return filtered_data
    if kind == "Sky":
        # Filtering the sky data
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
        return filtered_data





    return data


if __name__ == "__main__":
    print(get_data(place="London", forecast_days=3, kind="Temperature" ))