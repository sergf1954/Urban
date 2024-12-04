
# Задача "Функциональное разнообразие":
#
# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x,y : x==y, first, second)))

# Замыкание:
def get_advanced_write(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for j in data_set:
                if isinstance(j, str):
                  file.write(j + '\n')
                elif isinstance(j,list):
                  file.write((str(j)) + '\n')
                else:
                  file.write(str(j) + '\n')
    return write_everything

write = get_advanced_write('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'],'Еще одна строчка')

#Метод __call__:
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self, *words):
        return choice(list(self.words))

first_ball = MysticBall('Да','Да','Наверное','Вопрос','Привет')
print(first_ball())
print(first_ball())
print(first_ball())