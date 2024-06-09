def count_character_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
input_string = input("Enter a string: ")
character_frequency = count_character_frequency(input_string)
print("Character frequency:")
for char, freq in character_frequency.items():
    print(f"'{char}': {freq}")
