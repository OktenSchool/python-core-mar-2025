# # list
# # dict
# # tuple
# # numbers_tu = (1, 2, 3, 4, 5)
# # numbers_li = [11, 22, 33]
# # numbers_li[0]= 121
# # print(numbers_li)
#
# list = [11, 22, 33, 44, 55]
#
# list.append(1213)
# list.append(1214)
# print(list)
# del list[0]
# print(list)
# list.remove(33)
# print(list)
# list.insert(0, -100500)
# print(list)
#
# print(list[-2])
#
# aList = [1, 3, 5]
# bList = [2, 4, 6]
# result_list = [*aList, *bList, 123213]
# print(result_list)
# print(len(result_list))
#
# car_1 = dict(manufacturer='subaru', model='legacy', volume=2, status=False)
# print(car_1.keys())
# print(car_1.values())
# # car.clear()
# # print(car)
#
# car_2 = car_1.copy()
#
# car_2['model'] = 'brz'
#
# print(car_1)
# print(car_2)
#
# tuple_1 = (12,23,34,45,12)
# print(tuple_1)
# print(tuple_1[0]) # 12
# print(tuple_1.count(12))
#
#
#
#
#
#
#

car_1 = dict(manufacturer='subaru', model='legacy', volume=2, status=False)
car_2 = dict(manufacturer='bmw', model='650', volume=5, status=False)

# cars = [car_1, car_2, dict(manufacturer='porsche', model='cayenne', volume=4, status=False)]
# garage = []
#
# for car in cars:
#     garage.append(car)
#
# print(garage)


# even_numbers = []
# for x in range(100):
#     if x % 2 == 0:
#         even_numbers.append(x)
#
#
# print(even_numbers)

with open('tuple.txt') as file:
    for line in file:
        print(line)
