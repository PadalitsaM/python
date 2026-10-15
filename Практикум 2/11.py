from turtle import *
xc = float(input())
yc = float(input())
r = float(input())
x = float(input())
y = float(input())
screensize(10000, 10000)
scale = 2
tracer(False)
penup()
goto(xc * scale, yc * scale- r * scale)
pendown()
circle(r * scale)
d = (x - xc) ** 2 + (y - yc) ** 2
if d < r ** 2:
    print('Точка внутри окружности')
elif d == r ** 2:
    print('Точка лежит на окружности')
else:
    print('Точка вне окружности')
penup()
goto(x * scale,y * scale)
dot(8,'red')
tracer(True)
done()