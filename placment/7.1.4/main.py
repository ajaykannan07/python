def string_length(string):
    return len(string)

def string_copy(string):
    return string[:]

def string_concatenate(string1, string2):
    return string1 + string2

def string_to_uppercase(string):
    return string.upper()

def compare_strings_alphabetical(string1, string2):
    return string1 < string2
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

print("Length of string 1:", string_length(string1))
print("Copy of string 1:", string_copy(string1))
print("Concatenation of string 1 and string 2:", string_concatenate(string1, string2))
print("Uppercase version of string 1:", string_to_uppercase(string1))
print("Comparing string 1 and string 2 for alphabetical order:", compare_strings_alphabetical(string1, string2))
