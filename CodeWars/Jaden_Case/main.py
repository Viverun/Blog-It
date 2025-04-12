# def to_jaden_case(string):
#
#     new_string = string.title()
#     return new_string
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
# Incorrect because Your function is mostly correct, but there's a subtle issue. The .title() method capitalizes the first
# letter of every word, but it might not work as expected for certain edge cases (e.g., words with apostrophes).

def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))