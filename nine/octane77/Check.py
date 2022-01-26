# name = "Emmanuel"
# name_with_white_space = "     Upah     "
# name_capitalize = name.capitalize()
# name.lower()
#
# # print(name)
# # print(name_capitalize)
# # print(name.lower())
# print(name_with_white_space)
# print(name_lstriped)
# print(name_rstriped)
# print(name_stripped)

# TODO
# Research Python String Methods

list_of_names = ["Ruth", "Shola", "Busola", "Otunba", "Emmanuel", "Bro"]
# print(len(list_of_names))
# for name in list_of_names:
#     # print(len(i))
#     print(len(name), name)
print()
value = "a"
minimum = 1000
# for i in range(len(list_of_names)):
#     length = len(list_of_names[i])
#     if minimum > length:
#         minimum = length
#         value = list_of_names[i]
# print(value)
# print(minimum)
# print()

longest_string = max(list_of_names, key=len)
print(longest_string)
print(max(list_of_names, key=len))
print(min(list_of_names, key=len))
print(list_of_names.__contains__("Gen"))
print(list_of_names.__len__())

for i in list_of_names:
    if(len(i)) == 5:
        print(i)
print()
class_a = ["Helen", "Paul", "Joe", "Rogen", "Motunrayo"]
class_b = ["David", "Johnson", "Esther", "Mofobi", "John"]
# class_c = class_a.
# print(class_c)

max_length = 0
for i in class_a, class_b:
    for j in i:
        if len(j) > max_length:
            max_length = len(j)
            max_word = j
            position = i.index(j)
print(max_word, position)



# value = ""
# minimum = 5
# for i in range(len(list_of_names)):
#     length = len(list_of_names[i])
#     if minimum > length:
#         minimum = length
#         value = list_of_names[i]
#     print(value)
#     print(minimum)
# print(max(list_of_names))
