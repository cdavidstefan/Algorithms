# def insertionSort(myList):
#     for i in range(1, len(myList)):
#         j = i -1
#         current_element = myList[i]
#         while (myList[j] > current_element) and (j >= 0):
#             myList[j + 1] = myList[j]
#             j -= 1
#         myList[j + 1] = current_element
#     return myList
#
# myList = [5, 12, 21, 34, 66, 61, 67, 79]
# insertionSort(myList)
# print(myList)
#
#
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while (arr[j - 1] > arr[j]) and j > 0:
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]
#             j -= 1
#     return arr
#
#
# arr = myList.copy()
# insertion_sort(arr)
# print(arr)


# def bubbleSort(array):
#     n = len(array)
#
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return  array

def insertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        current_element = array[i]
        while current_element < array[j] and j >=0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_element
    return array





array = [5, 22232, 2, 43, 21, 676, 99, 91, 554,34534, 0,34, 4]
sorted_array = insertionSort(array)
print(sorted_array)