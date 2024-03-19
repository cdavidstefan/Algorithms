# map, filter, zip, reduce

# map -------------------------------------------------
# map(action, iterable)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def multiply_by_2(item):
    return item * 2
    # new_list = []
    # for item in li:
    #     new_list.append(item * 2)
    # return new_list


print(list(map(multiply_by_2, my_list)))
print(my_list)  # my list is not modified.

# filter ----------------------------------------------


def only_even(item):
    return item % 2 == 0


print(list(filter(only_even, my_list)))

# zip --------------------------------------------------
# zips item into a tuple, by index

your_list = [12, 13, 14, 15]
their_list = [16, 17, 17, 18]

print(list(zip(my_list, your_list, their_list)))

# reduce ------------------------------------------------