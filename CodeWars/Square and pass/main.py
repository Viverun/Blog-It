# while True:
#     try:
#         name = int(input("Enter Integer: "))
#         name = str(name)
#         # count = 0
#         total = ""
#         # total = str(total)
#         for element in name:
#             element = int(element)
#             # count += count
#
#             squared = element**2
#
#             squared = str(squared)
#             total += squared
#
#         total = int(total)
#         print(total)
#         break
#     except ValueError as e:
#         print("Please Enter a valid input")

def square_digits(num):
    num = str(num)
    total = ""
    for each_element in num:
        each_element = int(each_element)
        squared = each_element**2
        squared = str(squared)
        total += squared
    return int(total)
print(square_digits(123))






