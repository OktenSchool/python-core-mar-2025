# def user_builder(id, name):
#     user = dict(id=id, name=name)
#     return user
#
#
# u_1 = user_builder(1, 'abrikos')
# print(u_1)  # save to database / xls/ send to site
#
# u_2 = user_builder(2, 'tomat')
# print(u_2)


# strings = ['asd', 'qwe', 'zxc', 'jjhgjh']
# for item in strings:
#     print(item)
#
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)
#
# users = [{'id': 1, 'name': 'vasaya'}, {'id': 2, 'name': 'petya'}]
# for item in users:
#     print(item)


strings = ['asd', 'qwe', 'zxc', 'jjhgjh']
numbers = [1, 2, 3, 4, 5]
users = [{'id': 1, 'name': 'vasaya'}, {'id': 2, 'name': 'petya'}]

# def looper(arr):
#     for item in arr :
#         print(item)
# looper(strings)

# def looper2(arr1, arr2):
#     for item1 in arr1:
#         print(item1)
#
#
#     for item2 in arr2:
#         print(item2)

# def looper3(*args):
#     for asd in args:
#         print(asd)
#
#
# looper3([123, 345], [4, 6678, 79])

#
# def good_morning(problem):
#     print(problem)
#     print('прокинулись')
#     print('сходили в туалет')
#     print('ледве не впали після 40 хвилин')
#     print('постояди поки ноги придуть в норму')
#     print('попили водички')
#
#
# good_morning('проблема в тому що сьогодні понеділк')
# good_morning('проблема в тому що сьогодні вівторок')
# good_morning('проблема в тому що сьогодні середа')
# good_morning('проблема в тому що сьогодні четверг')

def reader(x):
    accum=''
    with open(x, encoding='utf-8') as file:
        for line in file:
            accum+=line
    return accum


result1 = reader('tuple1.txt')
print(result1)
result2 = reader('tuple2.txt')
print(result2)

print('ashdgahsdgashdb')
