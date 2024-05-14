# decorators supercharge our functions and allow us to extend the functionality

# in python, functions are first class citizens.
# they can be passed around like variables

# def hello(func):
#     return func()
#
#
# def greet():
#     print("still here")
#
#
# a = hello(greet)
# print(a)

# ------------------------------------------------------------------------------------------

# Higher Order Function - HOF. what are they?
# is a function that accepts as a parameter another function
# or a function that returns another function
# map, filter are HOC


# def greet(func):
#     func()
#
#
# def greet2():
#     def func():
#         print("5")
#     return func()
#
#
# print(greet(greet2))


# ------------------------------------------------------------------------------------------


# def my_decorator(func):  # tot ce stie functia asta sa faca este sa returneze ce returneaza functia din interior
#     def wrapper_func():  # doar ruleaza functia (variabila) primita ca si parametru in functia care o cuprinde
#         func()
#         print("my friend!")
#     return wrapper_func
#
#
# @my_decorator
# def hello():
#     print("Helloooo")
#
#
# @my_decorator
# def bye():
#     print("byeeeee")

# -------------------------------- acelasi lucru cu: -----------------------------------------


# def my_decorator(func):
#     def wrapper_func():
#         func()
#         print("my friend!")
#     return wrapper_func  # aici nu trebuie rulata functia wrapper_func, returneaza functia, nu apelul functiei
#
#
# # @my_decorator
# def hello():
#     print("Helloooo")
#
#
# def bye():
#     print("byeeeee")
#
#
# hello2 = my_decorator(hello)  # invelim functioa hello in functia my_decorator si o salvam intr-o variabila
# # b = my_decorator(bye)
#
# hello2()  # pe care o apelam
# my_decorator(hello)()  # sau

# inglobam / invaluim functia in decorator


# --------------------------------------------------------------------------------------------
# decorator pattern in programming. flexibility
# def my_decorator(func):
#     def wrapper_func(*args, **kwargs):
#         print("oh")
#         func(*args, *kwargs)  # unpack all the arguments
#         print("my friend!")
#     return wrapper_func
#
#
# @my_decorator
# def hello(greeting, emoji=":)"):
#     print(greeting, emoji)
#
#
# hello("hiiiiiii")

# a = my_decorator(hello)
# a('hiiii', ':)')


# ---------------------- practical application of decorators ---------------------------------

# @classmethod
# @staticmethod
# from time import time
#
#
# def performance(func):
#     def wrapper_func(*args, **kwargs):
#         t1 = time()
#         result = func(*args, **kwargs)
#         t2 = time()
#         delta_t = t2 - t1
#         print(f"Function {func.__name__} took {delta_t} s to run.")
#         return result
#     return wrapper_func
#
#
# @performance
# def long_time():
#     for i in range(10000000):
#         i * 5
#
#
# @performance
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(0, n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j +1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
#
# array = list(range(1000, 0, -1))
# sorted_arr = bubble_sort(array)
# print(sorted_arr)
#
# long_time()


# --------------- Exercise: ----------------------------------------------------------------

# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:

user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper_function(user):
        if user.get('valid'):
            fn(user)
        else:
            print("User is not authenticated.")
    return wrapper_function

    # code here


@authenticated
def message_friend(user):
    print('message has been sent')


message_friend(user1)
