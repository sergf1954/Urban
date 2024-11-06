
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):

        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.number = number_of_floors
        self.name   = name

    def __del__(self):
        print(  f'{self.name} снесён, но он останется в истории')

    # def __str__(self):
    #     return f'Название: {self.name} '


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


del h2
del h3
print(House.houses_history)


