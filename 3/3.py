from math import sqrt
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))
if x>=0:
    x = sqrt(x)
else :
    x = -(-x)**(1/3)
print ('x = ', x)
if y>=0:
    y = sqrt(y)
else :
    y = -(-y)**(1/3)
print ('y = ', y)
if z>=0:
    z = sqrt(z)
else :
    z = -(-z)**(1/3)
print ('z = ', z)