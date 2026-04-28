# print("dfjkgb"    '111111')
# CRUD

# Create

cities_string = "Odesa + Lviv ++ Krakiv ++ Kyiv"
# cities_list = cities_string.split()
cities_list = cities_string.split('++')
print(cities_list)

empty_list = []

numbers = [1, 5, 6, 0, 5.6]
numbers.sort(reverse=True)
print(numbers)

products = [
    'milk',
    'pears',
    'bread',
    'salt',
    'dates',
    'cheese',
]

sister_products = [
    'cake',
    'fish',
]

print(products)

mixed = [
    1,
    90.6,
    'dvfgfvb',
    False,
    True,
    [555, 8888],
    [],
]


# Read
# get by index
if products:
    first_product = products[0]
    print(first_product)
    second_product = products[1]

    products_quantity = len(products)
    print(products_quantity)

    element_wanted = 3
    element_wanted_index = element_wanted - 1

    if products_quantity >= element_wanted:
        wanted_product = products[element_wanted_index]
        print(wanted_product)

    last_product = products[-1]
    print(last_product)
    first_product_back = products[-4]
    print(first_product_back)


# for each

print("*" * 50)
total_product_words_length = 0
words_chain = ''

for product in products:
    current_product_word_length = len(product)
    # total_product_words_length = total_product_words_length + current_product_word_length
    total_product_words_length += current_product_word_length
    words_chain += f'-+{product}+-'

    print(111111111)
    if product == 'bread':
        continue
    # if product == 'dates':
    #     break
    print(product)

print(total_product_words_length)
print(words_chain)
print(5555555555555555555555555)

# Update
# change elem
products[-1] = 'apples'
print(products)

# add value
products.append('grapes')
print(products)

products.insert(0, 'potato')
print(products)

products.extend(sister_products)
print(products)

# Delete
is_838_in_string = '838' in 'fkjh838gjkdfgdf'
if not is_838_in_string:
    print(6666666666666666666666)
if is_838_in_string:
    print(888888888888888883333333333333888888888888)

is_potato_presented_in_product_list = 'potato' in products
if is_potato_presented_in_product_list:
    products.remove('potato')
print(products)

products.pop()
popped_product = products.pop(1)
print(popped_product)
print(products)

# sorting
products.reverse()

print(products)
products.sort(reverse=True)
print(products)
# print(products)
# print(products)

new_sorted_product_list = sorted(products, key=len)
# ['salt', 'milk', 'grapes', 'dates', 'cake', 'bread', 'apples']
# [4    ,    4  , 6,            5 ,     4,        5,       6]

print(new_sorted_product_list)




MESSAGE = 'ofhdgfids fdiuogydfi fd++++++++ {number}  {data}  {word}  ++++++++kdj {data}  fhgifdgy'
real_message = MESSAGE.format(number=55555, word='I am alpha and omega', data='Петро Петрович', ggg=55)
print(real_message)





