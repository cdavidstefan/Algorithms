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



def shellSort(myList):
    distance = len(myList) // 2

    while distance > 0:
        for i in range(distance, len(myList)):
            temp = myList[i]
            j = i

            while j >= distance and myList[j - distance] > temp:
                myList[j] = myList[j - distance]
                j = j-distance

            myList[j] = temp

        distance = distance // 2
    return myList
    
myList = [1, 5, 21, 41, 3, 9, 12]
print(shellSort(myList))