# Create a function that reverses a string:
# "Ana are mere!" -> "!erem era anA"

def reverse_string_1(string):
    # check if the input string is valid for reversal
    if not string or len(string) < 2 or type(string) is not str:
        print("Something's not right!")
    list_elements = list(string)
    new_list = []
    for i in range(len(list_elements)):
        new_list.insert(0, string[i])
    new_string = "".join(str(element) for element in new_list)
    return new_string


stringus = "Astăzi este 8 martie!"
print(list(stringus))
print(reverse_string_1(stringus))