first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x)-len(y) for x,y in zip(first, second) if len(x) - len(y))
#
second_result = ((bool(len(first[i]) == len(second[i])))
          if (len(first[i]) != len(second[i])) else True
          for i in range(len(first)))


print(list(first_result))

print(list(second_result))



# В переменную second_result запишите генераторную сборку,
# которая содержит результаты сравнения длин строк
# в одинаковых позициях из списков first и second.
# Составьте эту сборку НЕ используя функцию zip.
# Используйте функции range и len.
#