# Задача "Developer - не только разработчик"

class House:
    def __init__(self, name='ЖК Эльбрус',number_of_floors=30 ):
        self.number = number_of_floors
        self.name   = name

    def __len__(self):
        return self.number

    def __str__(self):
        return ('Название: ' + self.name + ' кол-во этажей ' + str(self.number))

    def go_to(self, new_floor):
        if new_floor > self.number or new_floor <= 0:
            print (f'Такого этажа не существует')
        else:
            for i in range(new_floor):
                print (i+1)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

h1.go_to(5)
h2.go_to(25)

print(h1)
print(h2)

print(len(h1))
print(len(h2))