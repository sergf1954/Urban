#    Домашняя работа по уроку "Перегрузка операторов"

class House:

    def __init__(self, name='ЖК Эльбрус',number_of_floors=30):
        self.number = number_of_floors
        self.name   = name


    def __len__(self):
        if isinstance(self.number, int):
            return self.number
        else:
            return False
    def __str__(self):
        return f'Название: {self.name} кол-во этажей {self.number}'

#################################################################

    ############################
    def __add__(self, other):
        #print("Print __add__  CALL")
        if isinstance(other, House):
            self.number = self.number + other.number

            return self
        if isinstance(other, int):
           self.number = self.number + other
           return self
        raise NotImplemented

    def __radd__(self, other):
        #print("Print __radd__  CALL")
        return self + other
    #########################  __iadd__
    def __iadd__(self, other):

        if isinstance(other, House):
            self.number += other.number
            return self
        if isinstance(other, int):
            self.number += other
            return self
        raise NotImplemented

    #############################
    ##########        Сравнение   ##########
    def __eq__(self, other):
        if other is None or not isinstance(other, House):
            return False
        return self.number == other.number
        #   больше
    def __gt__(self, other):
        if other is None or not isinstance(other, House):
            return False
        return self.number > other.number
        # больше равно
    def __ge__(self, other):
        if other is None or not isinstance(other, House):
            return False
        return self.number >= other.number

        # меньше
    def __lt__(self, other):
        if other is None or not isinstance(other, House):
            return False
        return self.number < other.number

        # меньше равно
    def __le__(self, other):
        if other is None or not isinstance(other, House):
            return False
        return self.number <= other.number
        # не равно
    def __ne__(self, other):
        if other is None or not isinstance(other, House):
            return False
        return self.number != other.number

    ################################################################
    def go_to(self, new_floor):
        if 0 <= new_floor < self.number:
            for i in range(new_floor):
                print(i + 1)
        else:
            print (f'Такого этажа не существует')

##############################
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__

print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
##############################
