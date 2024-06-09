def find_longest_word(string):
    words = string.split() 
    longest_word = max(words, key=len)  
    return longest_word

input_string = input("Enter a string: ")
longest_word = find_longest_word(input_string)
word_length = len(longest_word)

print("Longest word:", longest_word)
print("Number of characters in the longest word:", word_length)
