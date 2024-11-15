###################             Задача "Ошибка эволюции":
import random

class Animal:
    live              = True
    sound             = None         # звук (изначально отсутсвует)
    _DEGREE_OF_DANGER = 0            # степень опастности существа
    def __init__(self,  speed: int, _coord=None):
        if _coord is None:
            _coord = [0, 0, 0]
        self.coord = _coord
        self.speed = speed
    def move(self,dx, dy, dz):
        dx = dx * self.speed
        dy = dy * self.speed
        dz = dz * self.speed

        if dz < 0:
            print("t's too deep, i can't dive :(")
        else:
            self.coord[0] = dx
            self.coord[1] = dy
            self.coord[2] = dz

    def get_cords(self):
        print (f'X: {self.coord[0]} Y: {self.coord[1]} Z: {self.coord[2]} ')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f"Sorry, i'm peaceful :")
        else:
            print(f'Be careful, i'f'm attacking you 0_0 : ')

    def speak(self):
        print(self.sound)

class  Bird(Animal):
    beak = True
    @staticmethod
    def lay_eggs():
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):

        if self.speed/2-abs(dz) < 0:
            self.coord[2] = 0
        else:
            self.coord[2] = int(self.speed/2-abs(dz))
        pass
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"


db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1,2,3)
db.get_cords()
db.dive_in(6)
#print(Duckbill.mro())
db.get_cords()

db.lay_eggs()





