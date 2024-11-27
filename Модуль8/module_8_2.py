#Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"

def personal_sum(numbers):
    global incorrect_data
    incorrect_data = 0

    result = 0

    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            incorrect_data += 1
            print(f' Некорректный тип данных для подсчета суммы - {i}')
    return result


def calculate_average(numbers):
    col_poz = 0
    try:
        for i in range(len(numbers)):
            col_poz += 1
    except TypeError as esc:
        print(f'В numbers записан некорректный тип данных')
        return None
    try:
        summ = (personal_sum(numbers))
        summ = summ / (col_poz - incorrect_data)
    except ZeroDivisionError as ex:
        #print(f'Деление на ноль - {ex}')
        return 0

    return summ


print(f'Результат 1: {calculate_average("1, 2, 3")}')     # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')          # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')


