from abc import ABC, abstractmethod
from typing import Self
import random


class Character(ABC):
    DAMAGE = 25
    LIST = []

    def __init__(self, serial_number: str | int, payload: int):
        self.sn = serial_number
        self.hp = 100
        self.payload = payload
        self.victories = 0
        
        self.LIST.append(self)

    @abstractmethod
    def __str__(self) -> str:
        pass

    # def attack(self, other: 'Character'):
    def attack(self, other: Self):
        print(self, 'attack')
        if not self.is_alive:
            print(self, 'is dead, cannot be in fight')
            return

        if not self.has_weapon:
            print(self, 'is alive, but no weapon. Reload, now!!!!')
            return

        print(self, 'is going to attack', other)
        self.payload -= 1

        is_missed = random.choice([True, False, False])
        if is_missed:
            print('LOOSER', self, "MISSED")
            return
        other.hp -= self.DAMAGE
        print(other, 'OH MY')

    @property
    def has_weapon(self) -> bool:
        return self.payload > 0


    @property
    def is_alive(self) -> bool:
        return self.hp > 0

class Tank(Character):
    DAMAGE = 30
    def __str__(self) -> str:
        return f'Tank #{self.sn} with payload = {self.payload} and hp = {self.hp}'

class Artillery(Character):
    def __init__(self, serial_number: str | int, license: str):
        super().__init__(serial_number, payload=10000)
        self.lisense = license

    def __str__(self) -> str:
        return f'Arta #{self.sn} with payload = {self.payload} and hp = {self.hp} - YO_HO'

class Plane(Character):
    def __str__(self) -> str:
        return f'Plane {self.sn} is ready'


abrams = Tank(serial_number='abrams 123', payload=20)
t34 = Tank(11, payload=15)
boing777 = Plane(11, payload=15)
print(boing777)
arta1 = Artillery(231, license='usa')
arta2 = Artillery(2313, 'france')

abrams.attack(t34)
abrams.attack(t34)
t34.attack(abrams)
# abrams.attack()
# abrams.attack()
# abrams.attack()
# abrams.attack()
# t34.hp = 0
# t34.attack()
# abrams.attack()
# abrams.hp = 0
# abrams.attack()

print(abrams.__dict__)
print(abrams.DAMAGE)
abrams.DAMAGE = 33
print(abrams.__dict__)
print(t34.DAMAGE)
# print(t34.LIST)
# abrams.LIST.append(456456)
print(t34.LIST)
