# import pandas

# nums_1 = pandas.read_csv("file1.txt", header=None)[0].to_list()
# nums_2 = pandas.read_csv("file2.txt", header=None)[0].to_list()
# common_nums = [num for num in nums_1 if num in nums_2]


haha = "What is Airspeed Velocity of an Unladen Swallow"

dictionary = {word: len(word) for word in haha.split()}
print(dictionary)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp * 1.8 + 32 for (day, temp) in weather_c.items()}
print(weather_f)
