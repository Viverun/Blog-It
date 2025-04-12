# def disemvowel(string_):
#     enter_string = input("Enter the string: ")
#     for vowels in enter_string:
#         if (enter_string.contains( a || e || o || u)):
#
#     return string_
# def disemvowel(string_):
#     for elements in string_:
#         # print(elements)
#         if elements  == 'a':
#             continue
#         elif elements  == 'e':
#             continue
#         elif elements  == 'i':
#             continue
#         elif elements == 'o':
#             continue
#         elif elements  == 'u':
#             continue
#         # else:
#         #     print(elements)
#         string_ += elements
#     return string_
# print(disemvowel("Now where near the game"))

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result =""
    for char in string_:
        if char not in vowels:
            result += char
    return result
print(disemvowel("Now where near this"))





