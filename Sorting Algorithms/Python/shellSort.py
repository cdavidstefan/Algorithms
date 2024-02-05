# In pass one, instead of selecting immediate neighbors, we use elements that are at a fixed
# gap, eventually sorting a sublist consisting of a pair of data points. This is shown in the
# following diagram. In pass two, it sorts sublists containing four data points (see the
# following diagram). In subsequent passes, the number of data points per sublist keeps on
# increasing and the number of sublists keeps on decreasing until we reach a situation where
# there is just one sublist that consists of all the data points. At this point, we can assume that
# the list is sorted.

def shellSort(myList):
    n = len(myList)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = myList[i]
            j = i

            if j >= gap and myList[j - gap] > temp:
                myList[j] = myList[j - gap]
                j = j - gap
            
            myList[j] = temp

        gap = gap // 2
    return myList

myList = [1, 5, 21, 41, 3, 9, 12]
print(shellSort(myList))


# Find the mistake in the first one.
def secondShellSort(secondList):
    distance = len(secondList) // 2

    while distance > 0:
        for i in range(distance, len(secondList)):
            temp = secondList[i]
            j = i

            while j >= distance and secondList[j - distance] > temp:
                secondList[j] = secondList[j - distance]
                j = j-distance

            secondList[j] = temp

        distance = distance // 2
    return secondList
    
secondList = [1, 5, 21, 41, 3, 9, 12]
print(secondShellSort(secondList))