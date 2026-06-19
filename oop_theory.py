
class Person:
    def __init__(self, name: str, surname: str, weight: float):
        self.name = name.title()
        self.surname = surname.title()
        self.money = 0
        self.weight = weight

    def __str__(self) -> str:
        return f'<{self.full_name} with {self.money} grn - has status "{self.status}">'

    @property
    def full_name(self) -> str:
        return self.name + " " + self.surname

    @property
    def status(self) -> str:
        if self.money > 1000:
            return 'I am rich'
        return 'I am not too rich'

    def run(self):
        print(f'I, {self.name}, am running')
        self.weight -= 0.01

    def get_married(self, new_surname: str):
        self.surname = new_surname



person1 = Person(name='Petro', surname="Poroshenko", weight=55)
person2 = Person(name='Ivan', surname="Dub", weight=80)
person3 = Person(name='Natalka', surname="Lytvyn", weight=45)

person3.get_married(person2.surname)
print(     person3.full_name   )
print(     person3.status   )
print(person3)
print(person3.__dict__)

print(person1.__dict__)
name_person1 = person1.name
print(name_person1)

money_person1 = person1.money
print(money_person1)

person1.money += 200
person1.money += 300
person1.weight = 50
print(person1.__dict__)

person1.run()
person1.run()
person1.run()
person1.run()
person2.run()
print(person1.__dict__)

