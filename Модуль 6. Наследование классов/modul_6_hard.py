import math

class Figure:
    sides_count = 0
    def __init__(self, color, *sides:int, filled= True):
        if len(sides) != self.sides_count:
            j = []
            for _ in range(self.sides_count):
                j.append(1)
            pass
            self.__sides = j
        else:
            self.__sides = sides

        self.__color = color
        self.filled = filled
#  Начало Обработки атрибута COLOR
    # метод get_color возвращает список RGB цветов
    def get_color(self):    # Возвращает цвет по RGB
        return (self.__color)

    def __is_valid_color(self,r:int, g:int, b:int ):
        if r >= 0 and r <= 255:
            if g >= 0 and g <= 255:
                if b >= 0 and b <= 255:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def set_color(self,r:int, g:int, b:int ):
        if self.__is_valid_color(r,g,b):
            self.__color = [r,g,b]
            return self.__color
        else:
            return self.__color

#  Финал Обработки атрибута COLOR
#  Начало Обработки атрибута __SIDES
    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i
        return perimetr

    def get_sides(self):
        return self.__sides

    def is_valid_sides(self,*new_sides):
        number_of_sides = 0
        for _ in new_sides:
            number_of_sides +=1
## просмотреть на предмет, что числа все положительные
        # и кол-во новых сторон совпадает с текущим
        if (all(i > 0 for i in new_sides)
                and number_of_sides == self.sides_count):
## просмотреть на предмет, что числа все положительные
            return True
        else:
            return False

    def set_sides(self,*new_sides):
        j = []
        if self.is_valid_sides(*new_sides):
            for _ in range(self.sides_count):
                j = new_sides
            self.__sides = list(j)

    def set_sides_2(self, sides):
        self.__sides = sides  # надо для CUBE т.к. sides  с двумя __
#  Финал Обработки атрибута __SIDES

class Circle(Figure):
    sides_count = 1
    __radius = 0
    def __init__(self,color,*sides):
        super().__init__(color,*sides)
    def get_square(self):
        self.__radius = self.get_sides()[0] / 2 * math.pi

class Cube(Figure):
    sides_count = 12
    def __init__(self,color,*sides):
        super().__init__(color,*sides)
        self.__sides = sides
        if len(self.__sides) == 1:
            value = self.__sides[0]
        else:
            value = 1
        i = 0
        j = []
        while True:
            if i < self.sides_count:
                j.append(value)
                i += 1
            else:
                break
        self.__sides = j
        self.set_sides_2(self.__sides)

    def set_sides(self,*new_sides):
        i = 0
        j = []
        if len(new_sides) != 1:
            j = self.__sides
        if len(new_sides) == 1:
            while i < self.sides_count:
                j.append(new_sides[0])
                i += 1
                self.__sides = j
        self.set_sides_2(self.__sides)
    def get_volume(self):
        return self.__sides[0] ** 3

class Triangle(Figure):
    sides_count = 3

    def __init__(self,color,*sides):
        super().__init__(color,*sides)
        self.__sides = sides
    def get_square(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        p = len(self) / 2
        return math.sqrt(p * (p - a) * (p - b)* (p - c))


circle = Circle((200,200,200),10)
cube1 = Cube((222,35,130),6)

circle.set_color(55,66,77)
print(circle.get_color())

cube1.set_color(300,70,15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle.set_sides(15)
print(circle.get_sides())

print(len(circle))

print(cube1.get_volume())

##########
# triangle = Triangle((200, 200, 100), 10,15,6)
#
# print(triangle.get_sides(),' triangle')
# print(len(triangle), '  Периметр')
# print(triangle.get_square(), ' Площадь ' )


