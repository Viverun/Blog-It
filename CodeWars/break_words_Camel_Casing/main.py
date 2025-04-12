newword = ''
word = "newHello"
print_part1 = ""  # Stores first part before the capital letter
print_part2 = ""  # Stores second part including the capital letter

for index, letter in enumerate(word):
    if letter.isupper():
        print_part2 = word[index:]  # Store the second part from the capital letter onward
        break  # Stop the loop after finding the first capital letter
    print_part1 += letter  # Store the first part

# Print both parts on the same line with spacing
print(print_part1, print_part2)

print("\nFinal newword:", word)  # Just to confirm the full original word
