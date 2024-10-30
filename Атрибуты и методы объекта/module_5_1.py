# Задача "Developer - не только разработчик"


class House:
    def __init__(self, name='ЖК Эльбрус',number_of_floors=30 ):

        self.number = number_of_floors
        self.name   = name

    def go_to(self, new_floor):

        if new_floor > self.number or new_floor <= 0:
            print (f'Такого этажа не существует')
        else:
            for i in range(new_floor):
                print (i+1)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

