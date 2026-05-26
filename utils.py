def do_something():
    print(1111)
    pass


def is_number_bigger_than_10(number: float) -> bool:
    is_bigger_number = number > 10
    return is_bigger_number


def calculate_distance(velocity_km_per_hour: float, time_hours: float) -> float:
    if velocity_km_per_hour < 0 or time_hours < 0:
        # return 0
        raise ValueError('One of the numbers is negative')
    distance = velocity_km_per_hour * time_hours
    distance = round(distance, 2)
    return distance


def delete_file(filename: str) -> None:
    if not filename:
        raise FileNotFoundError(filename)
    print(f'I am deleting file {filename}')


def count_number_letters_in_sentence(sentence: str) -> int:
    sentence = sentence.replace(' ', '')
    number_letters = len(sentence)
    print(sentence, number_letters)
    return number_letters


def analyze_students_and_their_candy(students_data: dict[str, int]) -> tuple[int, int]:
    """
    first elem - students_number

    second - candies
    """
    students_number = len(students_data.keys())
    candies = sum(students_data.values())
    return students_number, candies


def get_admin_login() -> str:
    print('Go to database')
    return 'Alex65654'


def drive_together(driver: str, passenger_1: str = 'sister', passenger_2: str = '-', passenger_3: str = '-') -> str:
    pass_sms = f"{driver} + {passenger_1} + {passenger_2} + {passenger_3}"
    return pass_sms


sms = drive_together(driver='vova')
sms2 = drive_together('vova')
print(sms2)
data = {'alex': 6, 'marta': 55}
data_result_students, data_result_candies = analyze_students_and_their_candy(data)
print(data_result_students)


do_something()

is_bigger = is_number_bigger_than_10(5)
print(is_bigger)


print(type(5))

velocity = 10.5
time = 2.26587
way = calculate_distance(velocity, time)
print(way)
way2 = calculate_distance(time_hours=22, velocity_km_per_hour=655)
print(way2)

delete_file('jhr')
result = calculate_distance(5, 4)
counted = count_number_letters_in_sentence('dghgh h  h gffffh fghfghfgh                     ')
