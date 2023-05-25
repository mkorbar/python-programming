

# sting - str()
text = "to je nek text"

# celo stevilo - int()
the_answer = 42

# decimalna vrednost - float()
pi = 3.14

# boolova vrednost - bool()
is_may = True

# prazna vrednost
max_temp_today = None

#################################
# Lists (seznam)

empty_list = []
random_list = [None, None, "not so empty after all", 42, True, 3.14, [], ["element1", "element 2"]]

countries = ["Slovenia", "Austria", "Moldova", "New Zealand", "Malta", "Malta"]

# print(countries)
# # element z indexom 2
# print(countries[2])
# # seznam od el. 2 do konca
# print(countries[2:])
# # seznam od začetka do el. 2
# print(countries[:2])
# print(countries[1:3])
# print(countries[:-1])
# print(countries[-3:])

# # spreminjanje seznama
#
# countries.append("France")
# print(countries)
#
# first_country_in_the_list = countries.pop(0)
# print(countries)
# print(first_country_in_the_list)
#
# countries.sort()
# print(countries)

# # can not sort because it can not compare different types of variables
# # this will throw an error
# print(random_list)
# random_list.sort()
# print(random_list)

# for current_country in countries:
#     print(f"I have already been to {current_country}")


###################################################
# Dictionaries - Slovarji


packet_size = [10, 20, 30]

box = {"height_cm": [10, 11, 21], "width_cm": {"test": 20}, "length_cm": 30}
print(box)
print(box["width_cm"])
box['weight_kg'] = 50
print(box)
box['height_cm'] = 50
print(box)
box.pop("width_cm")
print(box)

