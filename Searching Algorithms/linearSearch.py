def linear_search(my_list, element):
    index = 0
    found = False
    # Match the value with each data element
    while index < len(my_list) and found is False:
        if my_list[index] == element:
            found = True
        index += 1
    return found

list = [2221, 33, 5, 66, 21, 45, 65, 32, 33, 56, 99, 7]
element1 = 2221
element2 = 10
print(linear_search(list, element2))