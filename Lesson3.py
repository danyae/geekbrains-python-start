# Числа, подключение модулей, функции справки
import os
import psutil
import sys
answer = input("Давайте поработаем (Y/N)")

if answer == 'Y':
    print("Я умею:")
    print("[1] - Вывести список файлов")
    print("[2] - Вывести информацию о системе")
    print("[3] - Вывести список процессов")
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
    else:
        pass
elif answer == 'N':
    print("До свидания!")
else:
    print("Неверный символ!")