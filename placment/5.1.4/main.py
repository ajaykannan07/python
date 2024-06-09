def display_array(arr):
    print("Current array:", arr)

def insert_element(arr, element, position):
    if position < 0 or position > len(arr):
        print("Invalid position to insert.")
        return arr
    return arr[:position] + [element] + arr[position:]

def delete_element(arr, position):
    if position < 0 or position >= len(arr):
        print("Invalid position to delete.")
        return arr
    return arr[:position] + arr[position+1:]

initial_array = []
n = int(input("Enter the number of elements in the array: "))
for _ in range(n):
    number = int(input("Enter a number: "))
    initial_array.append(number)

display_array(initial_array)


element_to_insert = int(input("Enter the element to insert: "))
position_to_insert = int(input("Enter the position to insert the element at (0-based index): "))

initial_array = insert_element(initial_array, element_to_insert, position_to_insert)
display_array(initial_array)
position_to_delete = int(input("Enter the position to delete the element from (0-based index): "))

initial_array = delete_element(initial_array, position_to_delete)
display_array(initial_array)
