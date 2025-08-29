import numpy as np

def array_attributes(arr):
    print("\nArray:\n", arr)
    print("Shape:", arr.shape)
    print("Data type:", arr.dtype)
    print("Number of dimensions:", arr.ndim)
    print("Size:", arr.size)
    print("Itemsize:", arr.itemsize)

def initialize_array(choice):
    if choice == 1:   # Normal array with user input
        n = int(input("Enter number of elements: "))
        elements = []
        for i in range(n):
            val = int(input(f"Enter element {i+1}: "))
            elements.append(val)
        return np.array(elements)

    elif choice == 2:   # Zeros array with user-defined shape
        r = int(input("Enter number of rows: "))
        c = int(input("Enter number of columns: "))
        return np.zeros((r, c), dtype=int)

    elif choice == 3:   # Ones array with user-defined shape
        r = int(input("Enter number of rows: "))
        c = int(input("Enter number of columns: "))
        return np.ones((r, c), dtype=float)

    elif choice == 4:   # Arange array
        start = int(input("Enter start value: "))
        end = int(input("Enter end value: "))
        step = int(input("Enter step value: "))
        return np.arange(start, end, step)

    elif choice == 5:   # Reshaped array
        r = int(input("Enter number of rows: "))
        c = int(input("Enter number of columns: "))
        total = r * c
        print(f"Enter {total} elements:")
        elements = []
        for i in range(total):
            val = int(input(f"Enter element {i+1}: "))
            elements.append(val)
        return np.array(elements).reshape(r, c)

    else:
        print("Invalid choice! Default array created.")
        return np.array([1, 2, 3])

def menu():
    print("\n=== Array Initialization Menu ===")
    print("1. Normal Array (user input)")
    print("2. Zeros Array")
    print("3. Ones Array")
    print("4. Arange Array")
    print("5. Reshaped Array")
    print("0. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting program...")
            break

        arr = initialize_array(choice)
        array_attributes(arr)
