from models import Person, Bank


def main():
    masha = Person('masha')
    alex = Person('alex')
    borys = Person('Borys')

    raif = Bank('raiffeisen')
    universal = Bank('universal')

    raif.open_account(borys)
    raif.open_account(borys)
    bank_account_alex = raif.open_account(alex)
    bank_account_alex.deposit(200)
    bank_account_borys = universal.open_account(borys)
    bank_account_borys.deposit(1000)
    bank_account_borys.deposit(1000)

    print(bank_account_borys)
    print(borys.__dict__)
    print(raif.__dict__)
    print(universal.__dict__)
    bank_account_borys.transfer_money(bank_account_alex, 533)
    print(borys.money)
    print(alex.money)
    print(raif.money)
    print(universal.money)

    print(borys >= alex)
    print(borys < raif)


main()
