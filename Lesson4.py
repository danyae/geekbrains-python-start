# Цикл while, списки
import os
import psutil
import shutil
import sys

answer = ''
while answer != 'q':
    answer = input("Давайте поработаем (Y/N/q)")
    if answer == 'Y':
        print("Я умею:")
        print("[1] - Вывести список файлов")
        print("[2] - Вывести информацию о системе")
        print("[3] - Вывести список процессов")
        print("[4] - Продублировать файлы в текущей директории")
        print("[5] - Дублировать файл")
        print("[6] - Удалить дубликаты файла в выбранной директории")
        do = int(input("Укажите номер действия:"))

        if do == 1:
            print(os.listdir())
        elif do == 2:
            print("Текущая директория:", os.getcwd())
            print("ОС:", sys.platform)
            print("Кодировка файловой системы:", sys.getfilesystemencoding())
            print("Логин пользователя:", os.getlogin())
            print("Количество CPU:", os.cpu_count())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("Дублирование файлов в текущей директории")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                if os.path.isfile(file_list[i]):
                    new_file = file_list[i] + ".dupl"
                    shutil.copy(file_list[i], new_file)
                i += 1
        elif do == 5:
            print("Дублирование выбранного файла")
            print("Список файлов:")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                if os.path.isfile(file_list[i]):
                    print(i, ": ", file_list[i])
                i += 1
            dupl_num = int(input("Введите номер файла"))
            if dupl_num < 0 or dupl_num > len(file_list) - 1 or os.path.isfile(file_list[dupl_num]):
                print("Неверный номер файла")
                continue
            new_file = file_list[dupl_num] + ".dupl"
            shutil.copy(file_list[dupl_num], new_file)
        elif do == 6:
            print("Удалить дубликаты файлов в выбранной директории")
            dir_name = input("Введите имя директории")
            if not os.path.isdir(dir_name):
                print("Неверное имя директории")
                continue
            file_list = os.listdir(dir_name)
            i = 0
            while i < len(file_list):
                full_name = os.path.join(dir_name,file_list[i])
                if full_name.endswith(".dupl"):
                    print("Удаляем ", full_name)
                    os.remove(full_name)
                i += 1
            print("Дубликаты удалены")
        else:
            pass
    elif answer == 'N':
        print("До свидания!")
    else:
        print("Неверный символ!")