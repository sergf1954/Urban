#    Задача "Съедобное, несъедобное":
# Вариант исправленный

class Animal:
    alive = True                # (живой)
    fed   = False               # (накормленный),
    def __init__(self, name:str):
        self.name=name            # - индивидуальное название каждого животного
    def eat(self, food):
        if isinstance(food, Plant):  # вернет True
            if food.edible:
                print(self.name, 'съел ', food.name)
                self.fed = True
            else:
                print(self.name, 'не стал есть ', food.name)
                self.alive = False
        else:
            print(' Не попали')
        pass
class Plant:
    edible = False                # (съедобность),
    def __init__(self, name):
        self.name = name          # name - индивидуальное название каждого растения
#    Start наследники для Animal
class Mammal(Animal):
    pass

class Predator(Animal):               # a1 - Predator
    pass
#    End наследники для Animal

#   Start   наследники для Plant
class Flower(Plant):                  # p1 для a1
    pass

class Fruit(Plant):
    edible = True
#   End  наследники для Plant
# class Fr:
#     pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик самоцветик')
p2 = Fruit('Заводной апельсин')
#p3 = Fr()

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
#a1.eat(p3)
print(a1.alive)
print(a2.fed)