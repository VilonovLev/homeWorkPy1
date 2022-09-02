import math
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
day_weak = int(input("Введите день недели: "))

if 0 < day_weak < 6:
    print("Нет")
elif 5 < day_weak < 8:
    print("Да")
else:
    print("В неделе семь дней :)")
print()

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\nX Y Z Истинность")
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z , not (x or y or z) == (not x and not y and not z))
print()

# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
x = int(input("Введите координату Х "))
y = int(input("Введите координату Y "))

if x == 0:
    print("На оси У")
elif y == 0:
    print("На оси Х")
elif x > 0:
    if y > 0:
        print("I четверть")
    else:
        print("IV четверть") 
else:
    if y > 0:
        print("II четверть")
    else:
        print("III четверть")        
print()

# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).
plus = "+"
minus = "-"
greater = "меньше"
less = "больше"
mask = "'Х' {} 0 и до {}бесконечности \n'У' {} 0 и до {}бесконечности"
quadrant = int(input("Введите номер четверти: "))

if quadrant == 1:
    print(mask.format(less, plus , less, plus )) 
elif quadrant == 2:
    print(mask.format(greater, minus , less, plus ))
elif quadrant == 3:
    print(mask.format(greater, minus , greater, minus ))
elif quadrant == 4:
    print(mask.format(less, plus , greater, minus ))
else:
    print("Такой четверти нет!")
print()

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между 
# ними в 2D пространстве.
x1 = float(input("Введите Х1 "))
y1 = float(input("Введите Y1 "))
x2 = float(input("Введите Х2 "))
y2 = float(input("Введите Y2 "))

result = round(math.sqrt(pow((x1-x2),2) + pow((y1 - y2),2)),2)
print(f"Расстояние между точками: {result}") 

