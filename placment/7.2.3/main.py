def strcpy(destination, source, index=0):
    if source[index] == '\0':
        destination[index] = '\0'
        return destination
    destination[index] = source[index]
    return strcpy(destination, source, index + 1)


source_string = input("Enter the source string: ")
destination_string = [''] * (len(source_string) + 1)  

strcpy(destination_string, source_string)

print("Copied string:", ''.join(destination_string))
