b = int(6)
c = int(1)

# for i in range(b):
#     i -= 1
#     for j in range(c):
#         while c <= b:
#             c += 1
#         print(c, end=" ")
#     print()

# number = int(1)
# row = int(6)
# for number in range(number):
#     while number <= int(5):
#         number += int(1)
#         print(number, end=" ")
#
#     while row > number:
#         row -= int(1)
#         print(row, end=" ")

for row in range(1, 6):
    for col in range(1, row+1):
        print(col, end=" ")
    print()

for col in range(5, 0, -1):
    for row in range(1, col+1):
        print(col, end=" ")
    print()
# for col in range(6, 1, -1):
#     for row in range(1, row):
#         print(row, end=" ")
#     print()
