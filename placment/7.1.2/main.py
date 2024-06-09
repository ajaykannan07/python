def replace_first_occurrence(string, old_char, new_char):
    new_string = ""
    found = False
    for char in string:
        if char == old_char and not found:
            new_string += new_char
            found = True
        else:
            new_string += char
    return new_string

input_string = input("Enter a string: ")
old_character = input("Enter the character to replace: ")
new_character = input("Enter the new character: ")
result = replace_first_occurrence(input_string, old_character, new_character)
print("Result:", result)
