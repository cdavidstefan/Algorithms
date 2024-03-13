def merge_sorted_arrays(arr1, arr2):
    sorted_array = []
    array_1_item = arr1[0]
    array_2_item = arr2[0]
    i = 1
    j = 1

    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    while array_1_item or array_2_item:
        print(array_1_item, array_2_item)
        if array_1_item <= array_2_item:
            sorted_array.append(array_1_item)
            array_1_item = arr1[i]
            i += 1
        else:
            sorted_array.append(array_2_item)
            array_2_item = arr2[j]
            j += 1

    return sorted_array


array_1 = [0, 3, 4, 31]
array_2 = [4, 6, 30]

print(merge_sorted_arrays(array_1, array_2))
# function should output : [0, 3, 4, 4, 6, 30, 31]
