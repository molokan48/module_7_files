import os
import time

for root, dirs, files in os.walk(r'.'):
    for file in files:
        filepath = os.path.abspath(file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file} '
              f'Путь: {filepath} '
              f'Размер: {file_size} байт '
              f'Время изменения: {formatted_time} '
              f'Родительская директория: {parent_dir}')
