# The third algorithm presented in this chapter is the merge sort algorithm, which was developed in
# 1940 by John von Neumann. The defining feature of this algorithm is that its performance is
# not dependent on whether the input data is sorted. Like MapReduce and other big data
# algorithms, it is based on a divide and conquer strategy. In the first phase, called splitting,
# the algorithm keeps on dividing the data into two parts recursively, until the size of the
# data is less than the defined threshold. In the second phase, called merging, the algorithm
# keeps on merging and processing until we get the final result.

def mergeSort(my_List):
    if len(my_List) > 1:
        mid = len(my_List) // 2
        left = my_List[:mid]
        right = my_List[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_List[k] = left[i]
                i = i + 1
            else:
                my_List[k] = right[j]
                j = j + 1
            k = k + 1
        
        while i < len(left):
            my_List[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            my_List[k] = right[j]
            j = j + 1
            k = k + 1
    
    return my_List

my_List = [44, 16, 24, 83, 75, 25, 9, 22, 10]
mergeSortedList = mergeSort(my_List)
print(mergeSortedList)