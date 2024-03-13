# List methods --------------------------------------------------------------
print("\nLists ---------------------------------------------------------------\n")

basket = ['a', 'b', 'x', 'c', 'd', 'd', 'e']

print(basket.index('a'))
print('d' in basket)
print('x' in basket)
print(basket.count('d'))  # counts the occurrence of a specific item

# basket.sort()  # sorts the list in place (modifies the array)
print(sorted(basket))  # sorted function produces a new array
print(basket)
# new_basket = basket[:]
# new_basket = basket.copy()
basket.sort()
basket.reverse()
print(basket)

# reversing can be done with list slicing
print(basket[::-1])  # creates a new version

list_with_100_elements = list(range(100))
print(list_with_100_elements)

sentence = ''
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
# sentence.join creates a new string
# and the shorthand for this is:
new_sentence_2 = ' '.join(['whatever'])

print(new_sentence)

# really important difference ------------------------------------------------
# when we have a method we apply it like this: basket.method() like sort().
# but when we have a function we use it like this: function(basket) like sorted().

# list unpacking -------------------------------------------------------------

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# None - is a type of data that represents the absence of value - it's just nothing / Null in other languages.


# Dictionaries - or Hash Tables / Map / Objects -------------------------------
print("\nDictionaries ---------------------------------------------------------------\n")
# unordered key: value pair

dictionary = {
    'a': [1, 2, 3],
    'b': True,
    'x': 'hello'
}

my_list = [
    {
        'a': [1, 2, 3],
        'b': True,
        'x': 'hello'
    },
    {
        'a': [4, 5, 6],
        'b': True,
        'x': 'hello'
    }
]

print(my_list[0]['a'][2])
print(dictionary['a'][1])

# when to use a data structure and when to use other?
# a dictionary has no order, a list is ordered.
# some information doesn't need to be ordered, like user properties
# we can use dictionaries; they also hold more information

# dictionary_2 = {
#     123: [1, 2, 3],
#     'b': True,
#     [100]: 'hello'
# }

# print(dictionary_2[123])
# print(dictionary_2[[100]])  # unhashable type 'list'

# a dictionary key always has to be immutable - a key cannot change.
# we can use a tuple as a key though
# usually a key in a dictionary is something descriptive and unique
# if we add another key with the same value, it will overwrite the first one

user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

user_2 = dict(name='JohnJohn')

print('size' in user)
print('greet' in user.keys())
print('hello' in user.values())
print(user.items())
# print(user_2.clear())

user_3 = user_2.copy()
print(user.get('age', 27))
print(user_2.clear())
print(user_3, 'user 3 still has the old information')
print(user.popitem())  # no longer random. removes the last key:value that
# was inserted into the dictionary.
# remember, dictionaries are not ordered so there is no "last" item

# noinspection PyTypeChecker
print(user.update({'age': 55}))
print(user)


# Tuples -------------------------------------------------------------------
print("\nTuples ---------------------------------------------------------------\n")

# immutable - has only two methods count() and index()
# tuple object does not support item assignment
# we can acces elements, of course.
# it tells others programmers that a specific list should not be changed.
# makes code more predictable; it's less flexible but makes code slightly more performant.
# a tuple can be a valid key in a dictionary

tuple_example = (1, 43, 3, 54, 54, 55)
print(sorted(tuple_example))  # creates a new tuple
new_tuple = tuple_example[1:2]
x, y, z, *others = (1, 2, 3, 4, 5)
print(others)
print(new_tuple)  # if only has one item tends to have the comma
print(tuple_example.index(54))  # returneaza indexul primului element gasit.

# Sets --------------------------------------------------------------------
print("\nSets ---------------------------------------------------------------\n")
# Sets are unordered collections of UNIQUE objects
my_list_set = [1, 2, 2, 2, 3, 4, 5, 5, 5]
my_set = {1, 2, 3, 4, 5, 5, 5}
my_set.add(100)
my_set.add(2)
print(my_set)
print(set(my_list_set))

# set object does not support indexing
# the way we check if something exists:
print(1 in my_set)

# True power of sets comes from the following methods:

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8, 9, 10}

# .difference() - what is the difference between our sets when viewed from my set >>
print(set_1.difference(set_2))

# .discard() - discards an element if it finds it
# print(set_1.discard(5))
# print(set_1)

# .difference_update() - removes the common elements between sets
# print(set_1.difference_update(set_2))
# print(set_1)

# .intersection()
# print(set_1.intersection(set_2))
# print(set_1 & set_2)

# .isdisjoint() - means that some two sets have nothing in common
print(set_1.isdisjoint(set_2))  # returneaza false pentru ca au ceva in comun

# .issubset() - intuitiv
print(set_1.issubset(set_2))

# .issuperset() - intuitiv
print("Is C++ a superset of C?")


# .union() - unește doua seturi si elimina dublurile (returneaza un nou set)
print(set_1 | set_2)

# key to being a good programmer is the ability to know that there are
# specific tools that you can use. not memorization
