# pr19_03.py
'''Написана функция drawRectangle(t, side1, side2), в которой черепашка t рисует
прямоугольник с длнной side1 и шириной side2. Далее написана программа, которая просит ввести
координаты точки А, длину и ширину прямоугольника и рисует прямоугольник,
левая нижняя вершина которого точка А.'''
# Программа разработана Киреевым Павлом 26.11.19

import turtle
def F(a, b, side1, side2, ugol):
    c = (180 - ugol)/2
    turtle
    t = turtle.Turtle()
    t
    t.goto(a, b)
    t.forward(100)
    t.left(ugol*2)
    t.forward(100)
    t.left(c*2)
    t.forward(100)
def main():
    a = int(input('Введите точку x: '))
    b = int(input('Введите точку y: '))
    side1 = int(input('Введите длинну прямоугольника: '))
    side2 = int(input('Введите ширину прямоугольника: '))
    ugol = int(input('Введите ширину прямоугольника: '))
    F(a, b, side1, side2, ugol)
main()

