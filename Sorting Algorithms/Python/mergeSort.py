# Algoritm de sortare a elementelor unei liste in ordine crescatoare

def merge_sort(unordered_list):

    # Phase 1: Splitting the list
    if len(unordered_list) > 1:

        mid = len(unordered_list) // 2  # midpoint
        left = unordered_list[:mid]     # left half
        right = unordered_list[mid:]    # right half

        # in momentul in care functia nu se mai reapeleaza,
        # variabilele left si right stocheaza cate un singur element.
        # unde sunt stocate celelalte elemente?

        merge_sort(left)
        merge_sort(right)

        # Phase 2: Merging the splits
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unordered_list[k] = left[i]
                i = i + 1
            else:
                unordered_list[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            unordered_list[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            unordered_list[k] = right[j]
            j = j + 1
            k = k + 1

    return unordered_list


my_list = [44, 16, 83, 7, 67, 21, 34, 45, 10]
mergeSortedList = merge_sort(my_list)
print(mergeSortedList)



def merge_sort_2(arr):
    if len(arr) > 1:
        midpoint = len(arr) // 2
        left = arr[:midpoint]
        right = arr[midpoint:]

        merge_sort_2(left)
        merge_sort_2(right)

        # merge part

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k +=1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

arr = [44, 16, 83, 7, 67, 21, 34, 45, 10]
sorted_arr = merge_sort_2(arr)
print(sorted_arr)