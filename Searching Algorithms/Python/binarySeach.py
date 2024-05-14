# Cautarea binara este un algoritm de cautare intr-o multime sortata, care divide intervalul de cautare la jumatate.
# Scopul este sa se foloseasca de multimea soratata si sa reduca complexitatea timp la O(log N)
# (mai rapid decat cautarea secventiala care are o complexitate timp de O(n) - timp liniar - creste odata cu inputul)

# Prima abordare - returneaza index-ul elementului cautat
def binary_search_index(arr, target):
    first = 0
    last = len(arr) - 1
    target_index = -1

    while first <= last and target_index == -1:
        mid = (first + last) // 2
        if arr[mid] == target:
            target_index = mid
            return f'Element was found at index {target_index}'
        elif target < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return 'Element is not in the list.'


index = binary_search_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 22, 33, 44], 3)
print(index)


# A doua abordare - returneaza true/false daca elementul a fost gasit/nu
def binary_search_boolean(arr, target):
    first = 0
    last = len(arr) - 1
    was_found = False

    while first <= last and was_found is not True:
        mid = (first + last) // 2
        if arr[mid] == target:
            was_found = True
            return was_found
        elif target < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return False


found = binary_search_boolean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 22, 33, 44], 5)
print(found)


# A treia abordare - returneaza valoarea cautata, in caz contrar un mesaj.
def binary_search_value(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        if target == arr[mid]:
            return target
        elif target < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return 'Element was not found.'


value = binary_search_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 22, 33, 44], 544)
print(value)
