def bubbleSort(myList):
    n = len(myList)

    for i in range(n):
        # after each pass, the largest unsorted item moves up to the correct position
        # so with each iteration we have to sort n-i-1 items
        for j in range(0, n-i-1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList

myList = [2221, 33, 5, 66, 21, 45, 65, 32, 33, 56, 99, 7]
sortedList = bubbleSort(myList.copy())
print(sortedList)