class User:
    @staticmethod
    def sign_in():
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, range):
        self.name = name
        self.range = range

    def my_range(self):
        print(f'My maximum range is {self.range} meters.')

    def run(self):
        print('ran really fast')


class HybridCharacter(Wizard, Archer):
    def __init__(self, name, power, range_length):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, range_length)


hb1 = HybridCharacter('borgie', 50, 500)
print(hb1.run())


# MRO - method resolution order is a rule in python that says in which order are things inherited
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)
print(D.mro())


# class Toy:
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {
#             'name': 'Yoyo',
#             'has_dog': False
#         }
#
#     def __str__(self):
#         return f'{self.color}'
#
#     def __len__(self):
#         return 500
#
#     def __getitem__(self, i):
#         return self.my_dict[i]
#
#
#
# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str('action_figure'))
#
#
# print(len(action_figure))
#
# arr = [1,2,3]
#
# print(len(arr))
#
# print(action_figure['name'])


# my_numbers = {2, 5, 3, 5, 4, 1, 2}
# doubled = len(my_numbers) * 2
# print(len(my_numbers))
# print(doubled)
#
# # var_1 = [x for x in range(20) if x / 2 == 0]
# # print(var_1)
#
# # char = 'cha'
# # cha = 'char'
# # print(len(char) * 'cha')
#
# lista = ['a', 'b', '12', 'cde']
# def functie(lista: list):
#     lista = [1, 2, 'abc']
#     new_list = []
#     for i in lista:
#         new_list.append(i)
#     return new_list
#
#
# functie(lista)
# print(functie(lista))