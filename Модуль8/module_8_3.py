
class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message



class Car:
    def __init__(self, model:str, __vin:int, __numbers:str):
        self.model   = model
        if self.__is_valid_vin(__vin):
            self.__vin = __vin
        if self.__is_valid_numbers(__numbers):
            self.__numbers = __numbers


    def __is_valid_vin(self,vin_number):
        if isinstance(vin_number, int):
            if 1000000<= vin_number <= 9999999:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номера')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers,str):
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
            else:
                return True
        else:
            raise IncorrectCarNumbers('Неверный тип данных для номеров')




try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  #print(exc.message)
  print(exc)
except IncorrectCarNumbers as exc:
    print(exc)
  #print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc)
except IncorrectCarNumbers as exc:
  print(exc)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc)
except IncorrectCarNumbers as exc:
  print(exc)
else:
  print(f'{third.model} успешно создан')

