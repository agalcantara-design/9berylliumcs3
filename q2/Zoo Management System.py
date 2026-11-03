class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

    def make_sound(self):
        return f"{self.name} makes a sound."

class Lion(Animal):
    def make_sound(self):
        return f"{self.name} roars loudly!."

    def eat(self):
        return f"{self.name} eats fresh meat."

class Elephant(Animal):
    def make_sound(self):
        return f"{self.name} trumpets!"

    def eat(self):
        return f"{self.name} eats grass and fruits."

class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} chatters!"

    def eat(self):
        return f"{self.name} eats bananas."

lion1 = Lion("Simba")
elephant1 = Elephant("Dumbo")
monkey1 = Monkey("George")


print(lion1.make_sound())
print(lion1.eat())
print(" ")

print(elephant1.make_sound())
print(elephant1.eat())
print(" ")

print(monkey1.make_sound())
print(monkey1.eat())
