def insertionSort(arr):

    # Parcurgem lista de la al doilea element (index 1) la capat
    for i in range(1, len(arr)):

        # in variabila j salvam indexul elemenului precedent elementului curent
        j = i - 1
        current_element = arr[i]

        # Ne imaginam un sir sortat (in stanga lui i) si sirul nostru nesortat (la dreapta de i)
        # cat timp elementul precedent este mai mare decat elemntul curent facem schimb de locuri
        # (il adaugam in sirul sortat din dreapta) si lungimea sirului sortat creste cu o unitate
        while (arr[j] > current_element) and j >= 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            # il decrementam pe j iar valoarea anterioara a lui j (j + 1) ia valoarea elemtului curent
            # repetam procesul (parcurgem bucla interioara de la dreapta la stanga)
            j -= 1
        arr[j + 1] = current_element

        # iesim din bucla interioara

    # returanm sirul sortat
    return arr


array = [5, 22232, 2, 43, 21, 676, 99, 91, 554,34534, 0,34, 4]
sorted_array = insertionSort(array)
print(sorted_array)





# def merge_sort(my_list):
#     # Incepem sortarea doar daca lista are mai mult de un element.
#     if len(my_list) > 1:
#         # Stabilim punctul de mijloc, jumatatea din stanga si jumatatea din dreapta
#         midpoint = len(my_list) // 2
#         left = my_list[:midpoint]
#         right = my_list[midpoint:]
#
#         merge_sort(left)
#         merge_sort(right)
#
#         i = 0
#         j = 0
#         k = 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 my_list[k] = left[i]
#                 i += 1
#             else:
#                 my_list[k] = right[j]
#                 j += 1
#             k += 1
#
#         while i < len(left):
#             my_list[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#             my_list[k] = right[j]
#             j += 1
#             k += 1
#
#     return my_list
#
#
# my_list = [99, 443, 1621, 24, 83, 1, 75, 25, 9, 22, 10]
# mergeSortedList = merge_sort(my_list)
# print(mergeSortedList)