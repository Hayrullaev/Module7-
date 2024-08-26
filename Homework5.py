import os
from time import localtime, strftime

directory = os.getcwd()
walk = os.walk(directory)
for root, dirs, files in walk:
    print(root, dirs, files)
    for file in files:
        full_path = os.path.join(root, file)
        print(file)

last_modified = os.path.getatime(full_path)
print('Файл', full_path, "быд последний раз изменен в", localtime(last_modified))

size = os.path.getsize(full_path)
print("Размер файла", full_path, "составляет", size, "байт")

root_dir = os.path.dirname(full_path)
print("Родительская директория файла", full_path, "это", root_dir)


