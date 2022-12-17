# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координаты x: '))
y = int(input('Введите координаты y: '))

if x > 0 and y > 0:
    print('Четверть I')
if x < 0 and y > 0:
    print('Четверть II')
if x < 0 and y < 0:
    print('Четверть III')
if x > 0 and y < 0:
    print('Четверть IV')
if x == 0 and y > 0 or x == 0 and y < 0:
    print('На оси y')
if x > 0 and y == 0 or x < 0 and y == 0:
    print('На оси x')
if x == 0 and y == 0:
    print('В центре плоскости')