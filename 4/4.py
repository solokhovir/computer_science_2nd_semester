import numpy as np
import matplotlib.pyplot as plt

a0 = float(input("Введите a0: "))
a1 = float(input("Введите a1: "))
a2 = float(input("Введите a2: "))
a3 = float(input("Введите a3: "))
a4 = float(input("Введите a4: "))

# функция
y = lambda x: a0+a1*x+a2*x**2+a3*x**3+a4*x**4
print("y:", y)

# создаѐм область, в которой будет
# - отображаться график
x = np.linspace(-5, 5, 42)
print(' x y(x)')
for temp in x :
    print ( temp, y(temp))

xmax = max(x,key=y)
print('Xmax = ',xmax,end=' ')

fmax = max(y(x))
print('Ymax = ',fmax)

xmin = min(x,key=y)
print('Xmin = ',xmin,end=' ')

fmin = min(y(x))
print('Ymin = ',fmin)

# создаѐм рисунок с координатную плоскость
fig = plt.subplots()

# значения x, которые будут отображены
# количество элементов в созданном массиве
# - качество прорисовки графика
# рисуем график
plt.plot(x, y(x))

# показываем график
plt.show()