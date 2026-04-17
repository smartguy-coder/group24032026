from letter_templates import LETTER
from poems import ENEIDA

poem = "first line\nsecond line"
# print(poem)

print(ENEIDA)

first_name = 'Donald'
# print(  id(first_name)  )
second_name = 'Trump'
island = "Ormuz"
ukraine = 'Україна'

# fullname = first_name + " " + second_name
fullname = f"{first_name} {second_name}"
# fullname = first_name + " " + second_name + "!!!" + " Hello on " + island + '!!!'
welcome_message = f"{fullname}!!! Hello on {island}!!!"
print(welcome_message)

letter1 = LETTER.format(fullname_data=fullname, island_data=island)
print(letter1)

letter2 = LETTER.format(fullname_data="Vasyl", island_data='Kuba')
print(letter2)
