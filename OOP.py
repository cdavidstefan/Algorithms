# OOP

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Cindy', 27)
player2 = PlayerCharacter('Lauren', 25)
player2.attack = '20 magic damage'

print(player1.run())
print(player2.age)
print(player2.attack)

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
