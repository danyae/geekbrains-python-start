# Цикл for, функции
import os
import psutil
import shutil
import sys


def duplicate_file(filename):
    if os.path.isfile(filename):
        new_file = filename + ".dupl"
        shutil.copy(filename, new_file)
        if os.path.exists(new_file):
            print("Файл ", new_file, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False


def sys_info():
    print("Текущая директория:", os.getcwd())
    print("ОС:", sys.platform)
    print("Кодировка файловой системы:", sys.getfilesystemencoding())
    print("Логин пользователя:", os.getlogin())
    print("Количество CPU:", os.cpu_count())


def remove_duplicates(dirname):
    file_list = os.listdir(dirname)
    count = 0
    for f in file_list:
        full_name = os.path.join(dirname, f)
        if full_name.endswith(".dupl"):
            print("Удаляем ", full_name)
            os.remove(full_name)
            count += 1
    print("Дубликаты удалены")
    return count


def double_files(dirname):
    file_list = os.listdir(dirname)
    i = 0
    while i < len(file_list):
        if os.path.isfile(file_list[i]):
            duplicate_file(file_list[i])
        i += 1


def main():
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
                sys_info()
            elif do == 3:
                print(psutil.pids())
            elif do == 4:
                print("Дублирование файлов в текущей директории")
                double_files(".")
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
                duplicate_file(file_list[dupl_num])
            elif do == 6:
                print("Удалить дубликаты файлов в выбранной директории")
                dir_name = input("Введите имя директории")
                if not os.path.isdir(dir_name):
                    print("Неверное имя директории")
                    continue
                print("Удалено ", remove_duplicates(dir_name), " файлов")
            else:
                pass
        elif answer == 'N':
            print("До свидания!")
        else:
            print("Неверный символ!")


if __name__ == "__main__":
    main()