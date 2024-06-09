def sum_of_elements(arr):
    total = 0
    for element in arr:
        total += element
    return total

numbers = []
n = int(input("Enter the number of elements in the array: "))
for _ in range(n):
    number = int(input("Enter a number: "))
    numbers.append(number)

sum_total = sum_of_elements(numbers)

print("The sum of the elements of the array is:", sum_total)
