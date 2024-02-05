# It is designed to make one swap for each
# pass, compared to N-1 passes with the bubble sort algorithm. Instead of bubbling the
# largest value toward the top in baby steps (as done in bubble sort, resulting in N-1 swaps),
# we look for the largest value in each pass and move it toward the top. So, after the first
# pass, the largest value will be at the top. After the second pass, the second largest value will
# be next to the top value. As the algorithm progresses, the subsequent values will move to
# their correct place based on their values. The last value will be moved after the (N-1)th pass.
# So, selection sort takes N-1 passes to sort N items.


def selectionSort(myList):
    for i in range(len(myList) - 1, 0, -1):
        min = 0
        for location in range(1, i + 1):
            if myList[location] > myList[min]:
                min = location
        myList[i], myList[min] = myList[min], myList[i]
    
    return myList

myList = [5,67,3,24,25,88,90,23]
print(selectionSort(myList))




def secondSelectionSort(secondList):
    for i in range(0, len(secondList) - 1):
        min_index = i
        for j in range(i + 1, len(secondList)):
            if secondList[j] < secondList[min_index]:
                min_index = j
        secondList[i], secondList[min_index] = secondList[min_index], secondList[i]
    
    return secondList

secondList = [5,67,3,24,25,88,90,23]
print(selectionSort(secondList))