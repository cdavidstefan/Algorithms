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


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        current_element = arr[i]
        while arr[j] > current_element and j >= 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
        arr[j + 1] = current_element
    return arr


arr = [5, 22232, 2, 43, 21, 676, 99, 91, 554,34534, 0,34, 4]
sorted_arr = insertion_sort(arr)
print(sorted_arr)

def insertion_sort_2(arr):
    n = len(arr)
    for i in range(1, n):
        current_element = arr[i]
        j = i - 1
        while arr[j] > current_element and j > 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
        arr[j + 1] = current_element
    return arr


sorted_arr_2 = insertion_sort_2(arr)
print(sorted_arr_2)