def sort_array(arr):
    return sorted(arr)
numbers = []
n = int(input("Enter the number of elements in the array: "))
for _ in range(n):
    number = int(input("Enter a number: "))
    numbers.append(number)
sorted_numbers = sort_array(numbers)
print("The sorted array in ascending order is:")
print(sorted_numbers)
