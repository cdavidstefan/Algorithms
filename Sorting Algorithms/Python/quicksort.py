
# Without list comprehension:
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quicksort(left) + middle + quicksort(right)


# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    midpoint_element = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for x in arr:
        if x < midpoint_element:
            left.append(x)
        elif x == midpoint_element:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)

array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(arr)
print(sorted_array)




# Using list comprehension:

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [3, 63, 82, 10, 1, 2, 12, 35]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)