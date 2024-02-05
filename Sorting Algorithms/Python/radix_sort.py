def radix_sort(arr):
    # Find the maximum number to determine the number of digits.
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit at the current place value
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Update count to store the actual position of each digit
    for i in range(1, 10):
        count [i] += count[i - 1]

    # Build the output array by placing elements in their correct position
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

# Example:

arr = [175, 45, 55, 75, 90, 240, 25, 2, 888]
radix_sort(arr)
print("sorted array:", arr)