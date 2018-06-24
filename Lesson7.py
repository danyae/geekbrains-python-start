#Разработка графического приложения

import turtle
import random
import math

PHI = 360 / 7  # Угол отклонения для 7 патронов
R = 50  # радиус окружности


def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def draw_barrel(x, y):
    gotoxy(x, y)
    turtle.circle(80)
    gotoxy(x, y+160)
    draw_circle(5, "red")  # мушка

    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(x+math.sin(phi_rad) * R, y+math.cos(phi_rad) * R + 58)
        draw_circle(22, "white")


def animate_barrel(x, y, start):
    gotoxy(x, y)

    for i in range(start, random.randrange(7, 50)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(x+math.sin(phi_rad) * R, y+math.cos(phi_rad) * R + 58)
        draw_circle(22, "brown")
        draw_circle(22, "white")

    gotoxy(x+math.sin(phi_rad) * R, y+math.cos(phi_rad) * R + 58)
    draw_circle(22, "brown")

    start = i % 7
    return start


turtle.speed(0)

draw_barrel(10, 10)

answer = ""
start = 0
while answer != "N":
    answer = turtle.textinput("Играть?", "Y/N")
    if answer == "Y":
        start = animate_barrel(10, 10, start)

        if start == 0:
            gotoxy(-150, 250)
            turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))
    else:
        pass