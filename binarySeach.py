def binarySearchIndex(myList, item):
    first = 0
    last = len(myList) - 1
    itemIndex = -1

    while (first <= last and itemIndex == -1):
        mid = (first + last) // 2
        if item == myList[mid]:
            itemIndex = mid
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return itemIndex

index = binarySearchIndex([1,2,3,4,5,6,7,8,9,10,11,12,13,15,18,22,33,44], 18)
print(index)



def binarySearchBoolean(myList, item):
    first = 0
    last = len(myList) - 1
    itemFound = False

    while (first <= last and itemFound == False):
        mid = (first + last) // 2
        if (item == myList[mid]):
            itemFound = True
        else:
            if (item < myList[mid]):
                last = mid - 1
            else:
                first = mid + 1
    return itemFound

found = binarySearchBoolean([1,2,3,4,5,6,7,8,9,10,11,12,13,15,18,22,33,44], 18)
print(found)


def binarySearchValue(myList, item):
    first = 0
    last = len(myList) - 1
    
    while first <= last:
        mid = (first + last) // 2
        if (myList[mid] == item):
            return myList[mid]
        else:
            if (item < myList[mid]):
                last = mid - 1
            else:
                first = mid + 1
    return None

value = binarySearchValue([1,2,3,4,5,6,7,8,9,10,11,12,13,15,18,22,33,44], 18)
print(value)