def count_subsets(n):
    return 2 ** n

n = int(input("Enter the number of distinct elements in the array: "))
total_subsets = count_subsets(n)
print("Total number of subsets:", total_subsets)
