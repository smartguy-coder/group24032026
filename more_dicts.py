# some_list = [2, 5, 6, 4]
#
# # for number in some_list:
# #     print(number)
# #
# # some_string = 'ajhdgfsjhds'
# # for letter in some_string:
# #     print(letter)
#
#
info = {
    'name': 'Alex',
    'age': 25
}
#
# # for item in info:
# for item in info.keys():
#     print(item)
#
#
# print(info)
# print(info.keys())
# print(info.values())
print(info.items())
#
# for item in info.values():
#     print(item)
#
#
# for item in info.items():
#     print('#' * 10)
#     key = item[0]
#     value = item[1]
#     print(key, value, 555, 6666)
#     print(item)
#     print('-----------------')

for key, value in info.items():
    print('#' * 10)
    item = key, value
    print(key, value, 555, 6666)
    print(item)
    print('-----------------')
#
#
# pair = ('name', 'Alex')
# # print(pair.count('name'))
# # print(pair.index('name'))
# # print(pair.index('Alex'))
#
# for item in pair:
#     print(item)

from pprint import pprint


some_list = ['Alex',]
pprint(some_list)


# some_tuple = ('Alex')  #  string
# some_tuple = ('Alex',) # tuple
some_tuple = 'Alex',     # tuple
print(type(some_tuple))
pprint(some_tuple)

some_difficult_tuple = ('Alex', 25, 80)
# name, age, weight = some_difficult_tuple
name, age, weight = 'Alex', 25, 80
# name = some_difficult_tuple[0]
# age = some_difficult_tuple[1]
# weight = some_difficult_tuple[2]
print(name, age, weight)
pprint(some_difficult_tuple)


# more_tuple_unpacking
some_difficult_tuple2 = ('Alex', 25, 80, 'tennis')
# some_difficult_tuple2 = ('Alex', 25)
user_name, user_age, *rest = some_difficult_tuple2
print(user_name, user_age)
print(rest)

name_of_user, *rest_data, weight, hobby = some_difficult_tuple2
print(name_of_user, hobby)
print(rest_data)






