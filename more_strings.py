name = '   2alEx6666666 bush 252 \n\n\n\n\n\n\n\n\n'

# name = name.strip()  # 'Alex 52'
name = name.strip(' \n2345')  # alEx bush
name = name.title()  # Alex Bush
name = name.swapcase()  # aLEX bUSH
name = name.capitalize()  # Alex bush
name = name.upper()  # ALEX BUSH
name = name.lower()  # alex bush
print(name)

# german_s = 'ß'.upper().lower()
# print(german_s)

# is has was can....
is_name_in_lowercase = name.islower()  # True False
# print(is_name_in_lowercase)
has_only_digits = '56565'.isdigit()
is_contains_only_lettres = "holJJlllik".isalpha()  # True False

if is_contains_only_lettres:
    print('Oh. Only letters in your nickname')

has_money = True
can_drive_car = False
is_odesa_big_city = True
##########################################################
admin_email = 'Alex@gmail.com'
admin_password = '123abc'
# --------------------------------------------------------


user_email_input = input("Enter user email: ").strip().lower()
user_password_input = input("Enter user password: ").strip()

is_admin_email = admin_email.lower() == user_email_input
print(is_admin_email)
is_admin_password_correct = admin_password == user_password_input
print(is_admin_password_correct)

if is_admin_email:
    print('is admin email')
    if is_admin_password_correct:
        print('ADMIN IS LOGGED IN')

print("finish")
