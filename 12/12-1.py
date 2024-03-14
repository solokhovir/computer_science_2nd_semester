# Метод половинного деления

def F(x):
    return x**3 - 3.2*x**2 + 4.84*x - 2.928

a = float(input("Введите a: "))
b = float(input("Введите b: "))
eps = float(input("Введите Eps: "))

while abs(b - a) > eps:
    x = (a + b) / 2
    if (F(x) == 0): break
    if (F(a) * F(x) > 0):
        a = x
    else:
        b = x

print('X = ', x)
print('F(X) = ', F(x))