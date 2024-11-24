# Домашнее задание по теме "Файлы в операционной системе"
import os
import time

directory = os.getcwd()

for root, dirs, files in os.walk(directory):
    for file in files:

        filepatch = os.path.join(root, file)
        filetime = os.path.getatime(directory)
        formatted_time = time.strftime("%d.%m.%Y %H:%M",
                                       time.localtime(filetime))

        file_size = os.path.getsize(filepatch)
        parent_dir = os.path.dirname(directory)

        print(f'Обнаружен Файл: {file}, Путь: {filepatch}, '
              f'Размер: {file_size},'
              f'Время изменения: {formatted_time},'
              f'Родительская директория: {parent_dir}')
