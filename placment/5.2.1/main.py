def remove_duplicates(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements


numbers = []
n = int(input("Enter the number of elements in the array: "))
for _ in range(n):
    number = int(input("Enter a number: "))
    numbers.append(number)

unique_numbers = remove_duplicates(numbers)
print("Unique values in the array:", unique_numbers)
