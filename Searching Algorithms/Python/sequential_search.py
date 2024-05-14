# Cautarea secventiala sau cautarea liniara este un algoritm de cautare comun
# Incepe de la un capat si itereaza prin elementele multimii pana cand este gasit elementul cautat.


def sequential_search_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr[i]
    return "Element not found."


output = sequential_search_element([1, 55, 23, 5, 87, 75], 88)
print(output)


def sequential_search_index(arr, target):
    index = 0
    while index < len(arr):
        if arr[index] == target:
            return f'Searched element was found at index {index}'
        index += 1
    return 'Element not found.'


output = sequential_search_index([1, 55, 23, 5, 87, 75], 75)
print(output)


def sequential_search_boolean(arr, target):
    found = False
    index = 0

    while index < len(arr):
        if arr[index] == target:
            found = True
        index += 1
    return found


output = sequential_search_boolean([1, 55, 23, 5, 87, 75], 234)
print(output)
