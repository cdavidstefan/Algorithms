def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i = i + 1
            else:
                myList[k] = right[j]
                j = j + 1
            k = k + 1
        
        while i < len(left):
            myList[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            myList[k] = right[j]
            j = j + 1
            k = k + 1
    
    return myList

myList = [44, 16, 24, 83, 75, 25, 9, 22, 10]
mergeSortedList = mergeSort(myList)
print(mergeSortedList)