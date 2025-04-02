# import datetime

from datetime import timezone, datetime, timedelta

# print(datetime.datetime.today())
# whatIsNow = datetime.now(timezone.utc)
# print(whatIsNow)
# now = datetime.now()
# print(now + timedelta(days=8))
# print(now.day)
# print(now.month)
# print(now.year)
# ===================================
import random

# print(random.random())
# print(random.randint(1,100))
# random_name = random.choice(['vasya', 'petya', 'anna', 'olha'])
# random_surname = random.choice(['shevchenko', 'franko', 'asd', 'qwe'])
# user = dict(name=random_name, surname=random_surname)
# print(user)
# print(random.choices(['vasya', 'petya', 'anna', 'olha'], [20, 1, 1, 1], k=1))

# ================================
import statistics


# print(statistics.harmonic_mean([90, 100]))
# print(statistics.mean([90, 100]))

def calculator(a, b):
    print(a, b)


# calculator(10, 20)
# calculator(20, 10)
# calculator(b=20, a=10)
values = dict(b=100, a=200)
# calculator(values['a'], values['b'])
calculator(**values)

users = [
    {'name': 'asd1', 'age': 3},
    {'name': 'asd2', 'age': 5},
    {'name': 'asd3', 'age': 7},
    {'name': 'asd4', 'age': 1},
]

# def sort_by_age(item):
#     return item['age']


print(sorted(users, key=lambda item: item['age']))


def rrrr(*xxx):
    print(xxx)


rrrr({'name': 'asd1', 'age': 3},
     {'name': 'asd2', 'age': 5},
     {'name': 'asd3', 'age': 7},
     {'name': 'asd4', 'age': 1})

random.randint(1, 10)
