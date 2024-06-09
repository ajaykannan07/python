def remove_repeated_characters(string):
    unique_characters = ""
    for char in string:
        if char not in unique_characters:
            unique_characters += char
    return unique_characters

input_string = input("Enter a string: ")
result = remove_repeated_characters(input_string)
print("String after removing repeated characters:", result)
