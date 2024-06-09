import math
def calculate_mean(arr):
    return sum(arr) / len(arr)
def calculate_deviation(arr, mean):
    return [x - mean for x in arr]
def calculate_variance(arr, mean):
    return sum((x - mean) ** 2 for x in arr) / len(arr)

numbers = []
n = int(input("Enter the number of elements in the array: "))
for _ in range(n):
    number = float(input("Enter a number: "))
    numbers.append(number)

mean = calculate_mean(numbers)

deviation = calculate_deviation(numbers, mean)

variance = calculate_variance(numbers, mean)

print(f"Numbers: {numbers}")
print(f"Mean: {mean}")
print(f"Deviation: {deviation}")
print(f"Variance: {variance}")
