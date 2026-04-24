
"""
ви пішли в кафе
вас 3
є страви 
- піцца 250
- кола 40
- соус 25

кожен каже скільки в нього є карманних грошей
визначити, яке максимальне замовлення можна зробити
"""
PIZZA_PRICE = 250
COLA_PRICE = 40
SAUCE_PRICE = 25

first_person_money = input('1 money: ')
first_person_money = float(first_person_money)
second_person_money = input('2 money: ')
second_person_money = float(second_person_money)
third_person_money = input('3 money: ')
third_person_money = float(third_person_money)

total_money = first_person_money + second_person_money + third_person_money
print(total_money)

full_menu_price = PIZZA_PRICE + COLA_PRICE + SAUCE_PRICE
pizza_cola_price = PIZZA_PRICE + COLA_PRICE
pizza_sauce_price = PIZZA_PRICE + SAUCE_PRICE

if full_menu_price <= total_money:
    print("We ordered all items")
elif pizza_cola_price <= total_money:
    print("We ordered pizza and cola")
elif pizza_sauce_price <= total_money:
    print("We ordered pizza and sauce")
else:
    print('No order')


