def find_largest_smallest(numbers):
    if not numbers:
        return None, None
    
    largest = smallest = numbers[0]
    
    for num in numbers[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    return largest, smallest

def main():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    largest, smallest = find_largest_smallest(numbers)
    if largest is not None and smallest is not None:
        print(f"Largest number: {largest}")
        print(f"Smallest number: {smallest}")
    else:
        print("No numbers provided.")

if __name__ == "__main__":
    main()
