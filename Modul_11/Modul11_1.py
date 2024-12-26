#                           Start requests
# urllib.request— Расширяемая библиотека для открытия URL-адресов
# модуль urllib в Python, предоставляет множество функций для работы
# с URL-адресами и веб-запросами,

# Пакет Requests рекомендуется для клиентского HTTP - интерфейса более высокого уровня.
# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# Requests — это модуль для языка Python, который используют для упрощения работы
# с HTTP-запросами.
#
import requests
#

r1 = requests.get('https://razlozhi.ru/patience-sol')
print(r1.text)

# загрузить картинку для последующего использования в Pillow

r2 = requests.get('https://ir-3.ozone.ru/s3/multimedia-n/wc1000/6743801219.jpg', stream=True)

with open('fialka54.jpg', 'wb') as image:
    for i in r2.iter_content(chunk_size=1024):
        image.write(i)

# #                          Finish requests#

# #                           Start Pillow
# # Pillow это форк PIL, основана на коде PIL.
# # Предоставляет поддержку при открытии, управлении
# # и сохранении многих форматов изображения.
#
#
from PIL import Image, ImageFilter

#  Загрузили картинку, посмотрели некоторые ее параметры: формат, размер,
try:
    picture = Image.open("fialka54.jpg")
    print("Размер изображения:")
    print(f'параметры  {picture.format},  {picture.size},  {picture.mode}')
    picture.show()
    picture.close()

    #  применили фильтр CONTOUR к изображению.

    img = Image.open("fialka54.jpg")
    img = img.filter(ImageFilter.CONTOUR)
    img.save("fialka54_C" + ".jpg")
    img.show()

    picture.close()

    # Создали миниатюру

    size = (128, 128)
    saved = "fialka54_m.jpg"
    img = Image.open("fialka54.jpg")
    img.thumbnail(size)
    img.save(saved)
    img.show()
    picture.close()
except FileNotFoundError:
    print("Файл не найден")

# #                           Finish Pillow

#                Start numpy
# Имеем матрицу двумерную, размером 5 строк 4 столбца.
# Имеем данные для изменения значений внутри матрицы.
# Делаем расчет по горизонтали и по вертикали (на уголок)
# Вывод: 1. исходная матрица.
#        2. входные данные.
#        3. результат

import numpy as np
#

def init_array(a,*num):
    i = 1
    s1 = 0
    s2 = 0
    s3 = 0
    p1 = 1
    while True:
        if i > len(a)-2:
            break
        else:
            a[i, p1] = str(num[i-1][0:1])[1:3]
            a[i, p1 + 1] = str(num[i-1][1:2])[1:3]
            a[i, p1 + 2] = int(a[i, 1]) + int(a[i, 2])
            s1 += int(a[i, 1])
            s2 += int(a[i, 2])
            s3 += int(a[i, 3])
            i += 1

    a[len(a) - 1, 1] = s1
    a[len(a) - 1, 2] = s2
    a[len(a) - 1, 3] = s3



print("Исходный массив")
a = np.array([['Месяц', '1 сумма', '2 сумма', 'сумма'],
               ['Январь', 2, 3, 4],
               ['Февраль', 3, 7, 8],
               ['Март', 4, 11, 12],
               ['Итого',5,1,1]])
print(a)
print(' Корректирующие данные')

zpt_num1 = (20,10)
zpt_num2 = (30,20)
zpt_num3 = (40,10)

print(f'{zpt_num1} - {zpt_num2} - {zpt_num3}')
init_array(a,zpt_num1,zpt_num2,zpt_num3)
print('Результирующий массив')

print(a)
print('--------------------------------------------')
print(' Размерность массива')
print(a.ndim)
print(' Размер массива')
print(a.shape)

#                Finish numpy