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





















# Acelasi algoritm cu implementare diferita;
# Impartim task-urile in doua functii.



# def merge_sort(arr):
#     if len(arr) > 1:
#         midpoint = len(arr) // 2
#         left = arr[:midpoint]
#         right = arr[midpoint:]
#
#         left = merge_sort(left)
#         right = merge_sort(right)
#
#         merge(left, right)
#
#     return arr
#
#
# def merge(left, right):
#     i = 0
#     j = 0
#     k = 0
#     sorted_array = []
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             sorted_array[k] = left[i]
#             i += 1
#         else:
#             sorted_array[k] = right[j]
#             j += 1
#         k += 1
#
#     while i < len(left):
#         sorted_array[k] = left[i]
#         i += 1
#         k += 1
#
#     while j < len(right):
#         sorted_array[k] = right[j]
#         j += 1
#         k += 1
#
#     return sorted_array
#
#
# list1 = [99, 443, 1621, 24, 83, 75, 25, 9, 22, 10]
# list2 = [3, 1, 9999]
# # mergeSortedList = merge_sort(list1)
# # print(mergeSortedList)
#
# sortedarr = merge(list1, list2)



# def merge_sort(my_list):
#     # Incepem sortarea doar daca lista are mai mult de un element.
#     if len(my_list) > 1:
#         # Stabilim punctul de mijloc, jumatatea din stanga si jumatatea din dreapta
#         midpoint = len(my_list) // 2
#         left = my_list[:midpoint]
#         right = my_list[midpoint:]
#
#         merge_sort(left)
#         merge_sort(right)
#
#         i = 0
#         j = 0
#         k = 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 my_list[k] = left[i]
#                 i += 1
#             else:
#                 my_list[k] = right[j]
#                 j += 1
#             k += 1
#
#         while i < len(left):
#             my_list[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#             my_list[k] = right[j]
#             j += 1
#             k += 1
#
#     return my_list
#
#
# my_list = [99, 443, 5000, 1621, 24, 83, 1, 75, 25, 9, 22, 10, 99999, 23, 13]
# mergeSortedList = merge_sort(my_list)
# print(mergeSortedList)