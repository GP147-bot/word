import numpy as np

# 1. Indexing

print("\n--- Indexing ---")
arr1 = np.array(list(map(int, input("Enter numbers for indexing (space-separated): ").split())))
index = int(input("Enter index to access (can use negative too): "))
print(f"Element at index {index}:", arr1[index])

# 2. Slicing

print("\n--- Slicing ---")
arr2 = np.array(list(map(int, input("Enter numbers for slicing (space-separated): ").split())))
start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))
step = int(input("Enter step value (default=1): ") or 1)
print(f"Sliced Array arr[{start}:{end}:{step}]:", arr2[start:end:step])

# 3. Reshaping + Transpose

print("\n--- Reshaping & Transpose ---")
arr3 = np.array(list(map(int, input("Enter numbers for reshaping (space-separated): ").split())))
rows = int(input("Enter number of rows for reshape: "))
cols = int(input("Enter number of columns for reshape: "))

if rows * cols == arr3.size:
    reshaped = arr3.reshape(rows, cols)
    print(f"\nReshaped Array ({rows}x{cols}):\n", reshaped)
    
    # Transpose
    transposed = reshaped.T
    print(f"\nTranspose of the Array ({cols}x{rows}):\n", transposed)
else:
    print(f"Reshape not possible! (Array size = {arr3.size}, but {rows}×{cols} = {rows*cols})")
