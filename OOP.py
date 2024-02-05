# OOP
# The 4 main pillars : encapsulation, abstraction, inheritance and polymorphism

class User():
    def sign_in(self):
        print('logged in successfully')

class Wizard(User):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        print(f'My attack deals {self.damage} magic damage!')

class Archer(User):
    def __init__(self, name, range):
        self.name = name
        self.range = range

    def attack(self):
        print(f'My maximum reach is {self.range} meters!')

wizard1 = Wizard("Gandalf", "500")
archer1 = Archer("Legolas", "5050")
wizard1.attack()
archer1.attack()










class PlayerCharacter:
    # Class object attribute:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def run(self):
        print('run')
        return 'done'

    def introduce_yourself(self):
        print(f'Hi! My name is {self.name} and i am {self.age} years old.')

    @classmethod
    def adding_numbers(cls, num1, num2):
        return cls('David', num1 + num2)

    @staticmethod
    def adding_numbers2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 27)
player2 = PlayerCharacter('Lauren', 25)

player3 = PlayerCharacter.adding_numbers(12,15)
player2.introduce_yourself()




class Car:
    def __init__(self, weight, max_speed, acceleration, color, traction):
        self.weight = weight
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.color = color
        self.traction = traction

    def honk(self):
        print('HONK!!')
        return None

rimac = Car('1000', '400', '50', 'gray', 'AWD')
porsche = Car('1234', '300', '40', 'powder_blue', 'AWD')
rimac.is_tunable = False
porsche.is_tunable = True

print(rimac.is_tunable)




