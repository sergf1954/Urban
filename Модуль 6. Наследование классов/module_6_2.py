#                 Задача "Изменять нельзя получать":
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'violet', 'yellow', 'black', 'orange']    # Атрибут класса
                              # в который записан список допустимых цветов для окрашивания.(Цвета
                              #написать свои)
    def __init__(self,owner:str, __model:str, __engine_power:int, __color:str):
        self.owner          = owner           #- владелец транспорта.(владелец может меняться)
        self.__model        = __model         #- модель(марка) транспорта.(мы не можем менять название модели)
        self.__engine_power = __engine_power  #- мощность двигателя.(мы не можем менять мощность двигателя самостоятельно)
        self.__color        = __color         # - название цвета.(мы не можем менять цвет автомобиля своими руками)
    def get_model(self):
        return (f'Модель:  {self.__model}')
    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}')
    def get_color(self):
        return (f'Цвет:  {self.__color}')

    def set_color(self,new_color:str):
        if new_color.upper() in str(self.__COLOR_VARIANTS).upper():
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}' )
    def owner(self,owner):
        self.owner = owner

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец :', self.owner)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500 , 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
