def merge_sorted_arrays(arr1, arr2):
    sorted_array = []
    i = 0
    j = 0

    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    while i < len(arr1) and j < len(arr2):
        print(arr1[i], arr2[j])
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1

    # Daca mai sunt elemente ramase in oricare din cele 2 array-uri:
    sorted_array.extend(arr1[i:])
    sorted_array.extend(arr2[j:])

    return sorted_array


array_1 = [0, 3, 4, 31, 445]
array_2 = [4, 6, 30, 229]

print(merge_sorted_arrays(array_1, array_2))
# function should output : [0, 3, 4, 4, 6, 30, 31]
