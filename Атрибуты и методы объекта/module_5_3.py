#    Домашняя работа по уроку "Перегрузка операторов"
from ctypes.wintypes import PRECT


class House:
    def __init__(self, name='ЖК Эльбрус',number_of_floors=30):
        self.number = number_of_floors
        self.name   = name


    def __eq__(self, other):
        if isinstance(other,House):
            return self.number == other.number
        else:
            return 'Не знаю что это '

    def __len__(self):
        if isinstance(self.number, int):
            return self.number
        else:
            return False
    def __str__(self):

        return f'Название: {self.name} кол-во этажей {self.number}'
##################################################
    # def __add__(self, other):
    #     if isinstance(other, int):
    #         return self.number + other
    #     else:
    #         return self.number
#################################################################
    def __add__(self, other):
        if isinstance(other, House):
            return House(self.number + other.number)
        else:
            return House(self.number + other)
    def __radd__(self, other):
        #ff= self.number
        return self.__add__(other)
################################################################
    def go_to(self, new_floor):
        if 0 <= new_floor < self.number:
            for i in range(new_floor):
                print(i + 1)
        else:
            print (f'Такого этажа не существует')



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 15)

#h1.go_to(5)
#h2.go_to(25)

print(h1)
#print(h2)

#print(h1 == h2)  # __eq__

h1 = h1 + 5  # __add__
print(h1)
#print(h1 == h2)  # __eq__