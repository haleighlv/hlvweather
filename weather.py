import csv
from datetime import datetime
from statistics import mean
import statistics
import string
import pandas as pd


DEGREE_SYMBOL = "\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celsius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celsius."
    """

    return f"{temp}{DEGREE_SYMBOL}"


# print(format_temperature(28))


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # object to store date
    date = datetime.fromisoformat((iso_string))
    format_date = date.strftime("%A %d %B %Y")
    return format_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:😄
        A float representing a temperature in degrees Celsius, rounded to 1 decimal place.
    """
    float_temp = float(temp_in_fahrenheit)
    celsius = (float_temp - 32) * 5 / 9
    celsius = round(celsius, 1)
    return celsius


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value."""
    total = sum([float(i) for i in weather_data]) / len(weather_data)
    return float(total)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    list = []
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if row != []:
                list.append([row[0], int(row[1]), int(row[2])])
    return list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data == []:
        return ()
    min_weather_data = [float(weather) for weather in weather_data]
    total_elements = len(min_weather_data)
    min_value = min_weather_data[0]
    last_index = -1
    for index, value in enumerate(min_weather_data):
        if min_value > value:
            min_value = value
        if value == min_value:
            last_index = index

    return (min_value, last_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data == []:
        return ()
    max_weather_data = [float(weather) for weather in weather_data]
    total_elements = len(max_weather_data)
    max_value = max_weather_data[0]
    last_index = -1
    for index, value in enumerate(max_weather_data):
        if max_value < value:
            max_value = value
        if value == max_value:
            last_index = index
    return (max_value, last_index)


# run_tests.py expects returning tuple


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    num_of_summary = len(weather_data)

    minimum = []
    maximum = []

    # converting input
    for daylist in weather_data:
        minimum.append(daylist[1])
        maximum.append(daylist[2])

    # temp_tuple = find_min(minimum)
    # min_temp = temp_tuple[0]
    # min_index = temp_tuple[1]
    min_temp, min_index = find_min(minimum)
    max_temp, max_index = find_max(maximum)
    average_min = calculate_mean(minimum)
    average_max = calculate_mean(maximum)
    day_min = convert_date(weather_data[min_index][0])
    day_max = convert_date(weather_data[max_index][0])
    return (
        f"{num_of_summary} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp))}, and will occur on {day_min}.\n "
        f" The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {day_max}.\n "
        f" The average low this week is {format_temperature(convert_f_to_c(average_min))}.\n "
        f" The average high this week is {format_temperature(convert_f_to_c(average_max))}.\n"
    )


# print(
#     generate_summary(
#         [
#             ["2020-06-19T07:00:00+08:00", 47, 46],
#             ["2020-06-20T07:00:00+08:00", 51, 67],
#             ["2020-06-21T07:00:00+08:00", 58, 72],
#             ["2020-06-22T07:00:00+08:00", 59, 71],
#             ["2020-06-23T07:00:00+08:00", 52, 71],
#             ["2020-06-24T07:00:00+08:00", 52, 67],
#             ["2020-06-25T07:00:00+08:00", 48, 66],
#             ["2020-06-26T07:00:00+08:00", 53, 66],
#         ]
#     )
# )


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    num_of_data = len(weather_data)

    day_list = []
    min_c_list = []
    max_c_list = []
    output = ""

    for i in range(num_of_data):
        day = convert_date(weather_data[i][0])
        day_list.append(day)
        min_c = convert_f_to_c(weather_data[i][1])
        format_min_c = format_temperature(min_c)
        min_c_list.append(format_min_c)
        max_c = convert_f_to_c(weather_data[i][2])
        format_max_c = format_temperature(max_c)
        max_c_list.append(format_max_c)
        output += f"---- {day_list[i]} ----\n  Minimum Temperature: {min_c_list[i].strip()}\n  Maximum Temperature: {max_c_list[i].strip()}\n\n"

    return output
