import random

city_names = ['Facts', 'London', 'Rome' , 'Berlin', 'Madrid']

# new_dict = {new_key: new_value for item in city_names}
city_temps = {city: random.randint(20, 30) for city in city_names}
print(city_temps)

# new_dict = {new_key: new_value for (key, value) in dict.items()}
above_25 = {city: temp for (city, temp) in city_temps.items() if temp > 25}
print(above_25)