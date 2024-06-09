def find_repetitive_element(arr):
    n = len(arr)
    total_sum = sum(arr)
    expected_sum = (n - 1) * (n - 2) // 2
    return total_sum - expected_sum

arr = [1, 2, 3, 4, 5, 6, 6, 7, 8]
repetitive_element = find_repetitive_element(arr)
print("The repetitive element is:", repetitive_element)
