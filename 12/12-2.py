# Метод Ньютона

def F(x):
    return x**3 - 3.2*x**2 + 4.84*x - 2.928

def F1(x):
    return 3*x**2 - 6.4*x + 4.84

x1 = float(input("Введите X0: "))
eps = float(input("Введите Eps: "))
x0 = x1 + 2*eps

while abs(x1 - x0) > eps:
    x0 = x1
    x1 = x0 - F(x0) / F1(x0)

print('X = ', x1)
print('F(X) = ', F(x1))