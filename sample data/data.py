import csv
import faker
import random

PEOPLE_COUNT = 100
MAX_BANK_ACCOUNTS_PER_PERSON = 4
MAX_HOMES_PER_PERSON = 2
MAX_CARS_PER_PERSON = 3
MAX_PHONES_PER_PERSON = 1

people = []
ssns = random.sample(range(10 ** 10, 10 ** 11), PEOPLE_COUNT)
accounts = []
account_ids = random.sample(range(10 ** 5, 10 ** 6), PEOPLE_COUNT * MAX_BANK_ACCOUNTS_PER_PERSON)
IBANs = set()
homes = []
postal_codes = random.sample(range(10 ** 9, 10 ** 10), PEOPLE_COUNT * MAX_HOMES_PER_PERSON)
cars = []
plates = random.sample(range(10 ** 4, 10 ** 5), PEOPLE_COUNT * MAX_CARS_PER_PERSON)
phones = []
numbers = random.sample(range(10 ** 8, 10 ** 9), PEOPLE_COUNT * MAX_PHONES_PER_PERSON)
f = faker.Faker(locale='fa-IR')
for _ in range(PEOPLE_COUNT):
    first_name = f.first_name()
    surname = f.last_name()
    ssn = ssns.pop()
    birth = f.date()
    city = f.city()
    work = f.company()
    address = f.address().replace('\n', ', ')
    people.append((first_name, surname, ssn, birth, city, work, address))
    for __ in range(random.randint(0, MAX_BANK_ACCOUNTS_PER_PERSON)):
        bank_name = random.choice(['ملی', 'ملت', 'تجارت', 'صادرات', 'سرمایه'])
        i = random.randint(10 ** 23, 10 ** 24)
        while i in IBANs:
            i = random.randint(10 ** 23, 10 ** 24)
        IBAN = 'IR{}'.format(i)
        account_id = account_ids.pop()
        accounts.append((ssn, bank_name, IBAN, account_id))
    for __ in range(random.randint(0, MAX_HOMES_PER_PERSON)):
        price = random.randint(5 * 10 ** 7, 10 ** 9)
        postal_code = postal_codes.pop()
        size = random.randint(80, 300)
        address = f.address().replace('\n', ', ')
        homes.append((ssn, price, postal_code, size, address))
    for __ in range(random.randint(0, MAX_CARS_PER_PERSON)):
        plate = str(plates.pop())
        plate = '{}{}{}'.format(plate[:2], random.choice(['ب', 'س', 'ط', 'ج', 'ی', 'ق', 'و', 'ر']), plate[2:])
        model = random.choice(['پراید', 'لامبورگینی', 'تیوتا', 'هیوندا', 'پژو', 'دنا', 'رانا'])
        color = f.safe_color_name()
        cars.append((plate, ssn, model, color))
    for __ in range(random.randint(0, MAX_PHONES_PER_PERSON)):
        operator = random.choice(['ایرانسل', 'رایتل', 'همراه اول'])
        number = '09{}'.format(numbers.pop())
        phones.append((ssn, number, operator))
print(people)
print(accounts)
print(homes)
print(cars)
print(phones)
with open('people.csv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerows(people)
with open('accounts.csv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerows(accounts)
with open('homes.csv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerows(homes)
with open('cars.csv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerows(cars)
with open('phones.csv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerows(phones)
