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

