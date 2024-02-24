def bubbleSort(myList):
    # stocam in variabila n valoarea lungimii sirului myList
    n = len(myList)

    # Parcurgem cu un for lista de la index 0 la n
    for i in range(n):

        # la fiecare traversare a sirului, cel mai mare element se deplaseaza la dreapta
        # drept urmare, dupa fiecare iteratie avand cel mai mare element in dreapta,
        # avem de parcurs cu i mai putin elemente de fiecare data (in bucla exterioara) de aceea n-i-1
        for j in range(0, n-i-1):

            # daca elementul de pe pozitia lui j este mai mare decat urmatorul, facem schimb de locuri
            # si tot asa pana in capat
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]

        # iesim din bucla interioara

    # returnam rezultatul
    return myList


myList = [2221, 33, 5, 66, 21, 45, 65, 32, 33, 56, 99, 7]
sortedList = bubbleSort(myList.copy())
print(sortedList)

# Complexitatea timp la bubble sort este O(n^2) in cel mai rau caz (o lista sortata descrescator)
# nu foarte eficient. simplu de implementat.
# nu foarte scalabil. se descurca din ce in ce mai slab pe masura ce creste inputul.


def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [2221, 33, 5, 66, 21, 45, 65, 32, 33, 56, 99, 7]
sorted_arr = bubble_sort(arr)
print(sorted_arr)