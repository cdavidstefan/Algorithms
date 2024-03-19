# Write a function that receives a list of integers and returns the highest
# even number

def highest_even(li):
    highest_even_number = 0
    for i in range(len(li)):
        if li[i] % 2 == 0 and li[i] > highest_even_number:
            highest_even_number = li[i]
        # do not prematurely exit the loop.
    return highest_even_number


def highest_even_2(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 44, 80, 11]))
print(highest_even_2([10, 2, 3, 44, 80, 11]))
# should return 10
