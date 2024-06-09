
def store_elements():
    arr = []
    n = int(input("Enter the number of elements you want to store: "))
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        arr.append(element)
    return arr


def display_elements(arr):
    print("The elements of the array are:")
    for i, element in enumerate(arr):
        print(f"Element {i+1}: {element}")

def main():
    array = store_elements()
    display_elements(array)

if __name__ == "__main__":
    main()
