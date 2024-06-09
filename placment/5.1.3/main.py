def search_element(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return f"Element found at position: {i}"
    return "Element not found"

array = [1, 2, 3, 4, 5, 6]
element_to_search = 4
result = search_element(array, element_to_search)
print(result)

