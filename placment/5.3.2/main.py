import math

def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n

def largest_not_perfect_square(numbers):
    largest = -1
    for num in numbers:
        if not is_perfect_square(num):
            if num > largest:
                largest = num
    return largest

n = int(input("Enter the number of integers: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

result = largest_not_perfect_square(numbers)
print("The largest number that is not a perfect square is:", result)
