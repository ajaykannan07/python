def are_strings_equal(string1, string2):
    return string1 == string2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_strings_equal(string1, string2):
    print("The two strings are equal.")
else:
    print("The two strings are not equal.")
