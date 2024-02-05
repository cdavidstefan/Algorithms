def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1

    # Initialize the count array to store the occurrences of each element
    count = [0] * range_of_elements

    # Count the occurrences of each element in the input array
    for num in arr:
        count[num - min_value] += 1

    # Update the count array to store the actual position of each element
    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    # Build the sorted output array
    output = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i] - min_value] - 1] = arr[i]
        count[arr[i] - min_value] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(len(arr)):
        arr[i] = output[i]


# Example usage:
arr = [4, 2, 2, 8, 3, 12, 33, 3, 1]
counting_sort(arr)
print("Sorted array:", arr)
