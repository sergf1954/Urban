import threading
import time


class Knight(threading.Thread):
    def __init__(self, name:str, power:int,enemies:int):
        super().__init__()
        #threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = enemies


    def battle(self,name, power, enemies):
        #enemies = 100   # Враги
        for i in range(1,enemies+1):
            time.sleep(1)
            enemies = enemies - power
            if enemies != 0:
                print(f'{name} сражается {i} день(дня) осталось {enemies} воинов')
            else:
                print(f'{name} сражается {i} день(дня) осталось {enemies} воинов')
                return i


    def run(self):
        print(f'{self.name} На нас напали ')
        end_battle = self.battle(self.name,self.power,self.enemies)    # финал битвы
        print(f'{self.name} одержал победу спустя {end_battle} день(дня)')


first_knight = Knight('Sir Lancelot', 10,100)
second_knight = Knight('Sir Galahad', 20,100)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()