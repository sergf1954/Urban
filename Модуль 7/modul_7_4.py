#   Домашнее задание по теме "Форматирование строк---"
#   Пример входных данных
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print('В команде Мастера кода участников: %d' % team1_num)
print('Итого сегодня в командах участников: %d и %d! ' %(team1_num,team2_num) )

print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print("Волшебники данных решили задачи за {}с!".format(team1_time))

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = (f'Победа команды Мастера кода!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = (f'Победа команды Волшебники Данных!')
else:
    result = (f'Ничья')
print(result)

time_avg = round((((team1_time / score_1) + (team2_time /score_2 )) / 2),2)

print(f'Сегодня было решено {score_1 + score_2} в среднем по\
 {time_avg} секунды на задачу! ')

