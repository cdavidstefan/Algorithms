def cycle_sort(arr):
    writes = 0

    for cycle_start in range(len(arr) - 1):
        item = arr[cycle_start]
        pos = cycle_start

        # Find the position where we put the element
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < item:
                pos += 1

        # If the element is already in the correct position, move to the next cycle
        if pos == cycle_start:
            continue

        # Otherwise, put the element to the correct position
        while item == arr[pos]:
            pos += 1

        arr[pos], item = item, arr[pos]
        writes += 1

        # Rotate the cycle
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1

            arr[pos], item = item, arr[pos]
            writes += 1

    return writes

# Example usage:
arr = [5, 2, 1, 4, 3]
cycle_sort(arr)
print("Sorted array:", arr)
