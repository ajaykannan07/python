def is_multiple_of_3(binary_string):
    state = 0

    for bit in binary_string:
        if bit == '1':
            if state == 0:
                state = 1
            elif state == 1:
                state = 2
            elif state == 2:
                state = 0
        elif bit == '0':
            if state == 0:
                state = 0
            elif state == 1:
                state = 2
            elif state == 2:
                state = 1

    return state == 0

binary_string = input("Enter a string of binary characters: ")
if is_multiple_of_3(binary_string):
    print("The binary string is a multiple of 3.")
else:
    print("The binary string is not a multiple of 3.")
