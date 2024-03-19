# map, filter, zip, reduce

# map -------------------------------------------------
# map(action, iterable)
my_list = [1,2,3,4,5]
def multiply_by_2(item):
    return item * 2
    # new_list = []
    # for item in li:
    #     new_list.append(item * 2)
    # return new_list


print(list(map(multiply_by_2, my_list)))
print(my_list)  # my list is not modified.
