
# Пример  raise ошибки
# def greet_person(person_name):
#     if person_name == 'ВоландДеМорт':
#         raise Exception('Мы не любим тебя ВоландДеМорт')
#     print(f' Привет {person_name}')
#
#
# greet_person('Петров')
# greet_person('ВоландДеМорт')

# class ProZero(Exception):
#     pass
#
# def f(a, b):
#     if b == 0:
#         raise ProZero(f"Деление на ноль невозмлжно")
#     return a / b
#
# print(f(10,0))

class ProZero(Exception):
    def __init__(self,message, extra_info):
        self.message = message
        self.extra_info = extra_info
def f(a,b):
    try:
        if b == 0:
            raise ProZero('Деление на ноль не возможно', {'a':a, 'b':b})
        return a / b
    except ProZero as e:
        print('Поймали ошибку')
        print(f'Сообщение об ошибки:  {e.message}')
        print(f'Доп информация - {e.extra_info}')
        return 'Ха-Ха'


print(f(10,0))