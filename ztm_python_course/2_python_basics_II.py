# conditional logic.
# if something execut a specific block of instruction
# else execute another block

# Truthy or Falsy - type conversion under the hood into bool
# all the values are considered truthy except for some that are falsy:
# None, False, 0, 0.0, 0j, [], {}, (), '' - empty stuff

# if something and something_else: do that

# expressions get evaluated in true or false.

# Ternary Operators ------------------------------------------------------
# they are also called conditional expressions

# ce fac ei? evalueaza o expresie si returneaza ceva in funcie de valoarea evaluata

# Short Circuiting -------------------------------------------------------

# In momentul in care interpretorul parcurge programul si intalneste o expresie de genul:
# if expresie_1 or expresie_2: do something
# el evalueaza prima expresie si daca ea este adevarata, cand intalneste cuvantul or
# nu mai evalueaza si a doua expresie pentru ca nu mai are de ce.
# poate fi foarte eficient in cazul in care cea de-a doua expresie este solicitanta dpdv computational
# la fel functioneaza si cu and. adica invers. Dar da.

# our friend the interpreter

# Logical Operators ------------------------------------------------------

# < > <= >= != and or not // not(False) == True !
# == checks for equality of value.
# is checks if the location in memory where a specific value is stored is the same as the other one
# 10 == 10.0 => True
# is works for primitives not for lists for example. or any other data structure.

# for loops - powerful concept in programming
# iterables - a collection that can be iterated - one by one checks each element in that collection.

# items().values().keys() - 3 useful methods in dictionaries.

# for key, value in dictionary:
#     print(key, value)

# ----------------------

# enumerate() - returneaza si indexul elemetelor din iterabil.
# foarte util daca avem nevoie si de indexul elementelor prin care trecem.

# using a for or a while really depends on the problem we are trying to solve.
# fixed number of steps in for

# while True:
#     response = input("Say something: ")
#     if response == 'bye':
#         break

# pass - placeholder. in cazul in care scriem cod, lucram la un program si vrem sa implementam o functie
# dar vrem sa implementam altceva inainte putem sa umplem linia de cod din interiorul functiei cu pass
# pentru ca interpretorul sa nu ne returneze o eroare, sa treaca peste linia respectiva de cod.
# when the interpretor hits "continue" does nothing and goes to the top of the enclosing loop.

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

print(len(picture[1]))

# end="" makes the print function not go to a new line by default after every print.

for row in picture:
    for pixel in row:
        if pixel:
            print('*', end='')
            print('*', end='')
        else:
            print(' ', end='')
            print(' ', end='')
    print('')

# best practices:
#   clean
#   readability
#   predictability
#   DRY - reusable code
