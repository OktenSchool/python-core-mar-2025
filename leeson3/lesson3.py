# # school = 'okten'
# # list = []
# #
# # for char in school:
# #     new_char = char + '!'
# #     list.append(new_char)
# #
# # print(list)
#
# # school = ' okten '
# # print(school.upper())
#
# phone = '+3 80 (63) 338-12-12'  # 0633381212
# result = (phone
#           .replace(' ', '')
#           .replace('-', '')
#           .replace('(', '')
#           .replace(')', '')
#           .replace('+38', ''))
# print(result)
#
# # print(result.isnumeric())
#
# print(result.find('12'))
#
# foo1 = '  asdasds'
# print(len(foo1))
#
# print(len(foo1.lstrip()))



with open('tuple.txt', encoding='utf-8') as file:
    for line in file:
        strip_line = line.rstrip()
        print(strip_line)
