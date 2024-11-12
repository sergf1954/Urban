#    Задача "Съедобное, несъедобное":

class Animal:
    alive = True                # (живой)
    fed   = False               # (накормленный),

    def __init__(self, name):
        self.name = name         # - индивидуальное  название  каждого  животного


class Plant:
    edible = False                # (съедобность),

    def __init__(self, name):
        self.name = name          # name - индивидуальное  название каждого  растения

#    Start наследники для Animal
class Mammal(Animal):

    def eat(self, food):
        print(self.name, 'съел ', food.name)
        self.fed = True


class Predator(Animal):                # a1 - Predator


    def eat(self, food):
        print(self.name, 'не стал есть ', food.name)
        self.alive = False

#    End наследники для Animal

#   Start   наследники для Plant
class Flower(Plant):                 # p1 для a1
    edible = False                   # (съедобность)


class Fruit(Plant):
    edible = True

#   End  наследники для Plant

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик самоцветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)