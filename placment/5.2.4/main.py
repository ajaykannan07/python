def are_arrays_same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True
array1 = []
n = int(input("Enter the number of elements in the first array: "))
for _ in range(n):
    number = int(input("Enter a number for the first array: "))
    array1.append(number)
array2 = []
n = int(input("Enter the number of elements in the second array: "))
for _ in range(n):
    number = int(input("Enter a number for the second array: "))
    array2.append(number)

if are_arrays_same(array1, array2):
    print("The arrays are same.")
else:
    print("The arrays are not same.")
