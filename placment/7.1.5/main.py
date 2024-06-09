def strlen(string):
    length = 0
    for char in string:
        length += 1
    return length

def strcpy(destination, source):
    for i in range(len(source)):
        destination[i] = source[i]
    return destination

def strcat(destination, source):
    dest_len = strlen(destination)
    for i in range(len(source)):
        destination[dest_len + i] = source[i]
    return destination

def strstr(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return i
    return -1

def strrchr(string, char):
    last_occurrence = -1
    for i in range(len(string)):
        if string[i] == char:
            last_occurrence = i
    return last_occurrence

string = "hello world"
substring = "world"
char_to_find = 'o'
destination = [' '] * 20 
print("Length of string:", strlen(string))
print("Copying string:", strcpy(destination, string))
print("Concatenating string:", strcat(destination, " concatenate"))
print("Finding substring:", strstr(string, substring))
print("Finding last occurrence of character:", strrchr(string, char_to_find))
