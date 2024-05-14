# Interclasarea a doi vectori consta in parcurgerea concomitenta a vectorilor selectand pe rand elementul
# mai mic dintre elementul curent din primul vector si elementul curent din al doilea vector, adaugandu-l
# intr-un nou vector ordonat crescator.

# ex: Input: a = [1, 2, 5, 9] si b = [3, 4, 5, 7] -> Output: c = [1, 2, 3, 4, 5, 5, 7, 9]

def interclasare(arr1, arr2):

    i = 0
    j = 0

    merged_list = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_list.append(arr1[i])
            i += 1
        else:
            merged_list.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged_list.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_list.append(arr2[j])
        i += 1

    return merged_list


output = interclasare([1, 2, 5, 9], [3, 4, 5, 7])
print(output)
