# It is designed to make one swap for each
# pass, compared to N-1 passes with the bubble sort algorithm. Instead of bubbling the
# largest value toward the top in baby steps (as done in bubble sort, resulting in N-1 swaps),
# we look for the largest value in each pass and move it toward the top. So, after the first
# pass, the largest value will be at the top. After the second pass, the second-largest value will
# be next to the top value. As the algorithm progresses, the subsequent values will move to
# their correct place based on their values. The last value will be moved after the (N-1)th pass.
# So, selection sort takes N-1 passes to sort N items.


def selection_sort(arr):
    # Salvam intr-o valriabila n lungimea sirului arr
    n = len(arr)

    # Parcurgem sirul de la primul element la ultimul (index=0 la n)
    for i in range(0, n):

        # Stocam intr-o variabila indexul celui mai mic element din sir.
        # Initial este valoarea lui i deoarece i incepe de la 0.
        minim = i

        # In bucla interioara parcurgem elementele din dreapta lui i (incepand cu i+1)
        # Ne imaginam la dreapta de i, sirul nostru (nesortat) si la stanga de i sirul sortat
        # in care se adauga, la fiecare iteratie, cel mai mic element gasit
        for j in range(i + 1, len(arr)):

            # Daca elementul de pe pozitia j (elementul curent) este mai mic decat elementul de pe pozitia minim
            # Inseamna ca am gasit un element mai mic in sirul nesortat si ii salvam indexul in variabila minim
            if arr[j] < arr[minim]:
                minim = j

            # iesim din bucla interioara

        # la fiecare parcurgere a listei, in bucla exterioara punem elementul minimim gasit
        # pe pozitia lui i
        arr[i], arr[minim] = arr[minim], arr[i]

    # returnam sirul sortat
    return arr


array = [1, 55, 32, 9, 214, 65, 2, 5454, 63, 3246, 25]
sorted_array = selection_sort(array)
print(sorted_array)


# Deoarece avem doua bucle una in alta (nested) complexitatea timp in cel mai rau caz este O(n^2)
# adica pentru fiecare element din lista trebuie sa facem n iteratii n * n
# i iteratii de n ori si j iteratii de n ori


# def selectionSort(myList):
#     for i in range(len(myList) - 1, 0, -1):
#         minim = 0
#         for location in range(1, i + 1):
#             if myList[location] > myList[minim]:
#                 minim = location
#         myList[i], myList[minim] = myList[minim], myList[i]
#
#     return myList
#
# myList = [5,67,3,24,25,88,90,23]
# print(selectionSort(myList))
#
#
#


#
# def secondSelectionSort(secondList):
#     for i in range(0, len(secondList)):
#         minim_index = i
#         for j in range(i + 1, len(secondList)):
#             if secondList[j] < secondList[minim_index]:
#                 minim_index = j
#         secondList[i], secondList[minim_index] = secondList[minim_index], secondList[i]
#
#     return secondList
#
# secondList = [5,67,3,24,25,88,90,23,999,1]
# print(selectionSort(secondList))
