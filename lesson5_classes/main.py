def gener_user(id, name):
    return {'id': id, 'name': name}


user_1 = gener_user(10, 'asdgasdhg')
print(user_1)


# def foobar(xxx: str):
#     print(xxx)
#
#
# foobar(100)

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def greeting(self):
        print('hello ' + self.name)


user1 = User(1, 'vasya')
user2 = User(2, 'petya')

user1.greeting()
user2.greeting()


# def print_user(obj:User):
#     print(obj)
#
#
# print_user('ahsgdhas')
# print_user(1231)
# print_user(user_1)
# print_user(user)


class Car:
    def __init__(self, model, price, year):
        self.model = model
        self.price = price
        self.year = year

    def change_year(self, year):
        if year > 1861:
            self.year = year

    def __str__(self):
        return 'model is - ' + self.model + ' price is - ' + str(self.price) + ' year is  - ' + str(self.year)


car1 = Car('asd', 123, 2015)
car1.change_year(1900)
print(car1.year)
# print(car1.model, car1.price, car1.year)
print(car1)

car2 = Car('qwe', 234, 2016)
# print(car2.model, car2.price, car2.year)
print(car2)


