from scipy import integrate

def F(x):
    return x**3+2*x-10

def INT_Count(Proc,f,a,b,eps,nmax):
    s0 = 0
    s = 1e25
    n = 2
    while(abs(s-s0)>eps) & (n<nmax):
        s0 = s
        n = 2*n
        s = Proc(f,a,b,n)
    return [s,n]

def Pr(f,a,b,n):
    h = (b - a) / n
    x = a + h / 2
    s = 0
    for i in range (n):
        s = s + f(x)
        x = x + h
    return h * s

def Tr(f,a,b,n):
    h = (b - a) / n
    x = a
    s = (f(a) + f(b)) / 2
    for i in range (1,n):
        x = x + h
        s = s + f(x)
    return h * s

def Simps(f,a,b,n):
    h = (b - a) / n
    x = a
    z = 1
    s = f(a) + f(b)
    for i in range (1,n):
        x = x + h
        s = s + (3 + z) * f(x)
        z =- z
    return h * s / 3

a = float(input("Введите a: "))
b = float(input("Введите b: "))
eps = float(input("Введите Eps: "))
nmax = int(input("Введите NMax: "))

[S,Err] = integrate.quad(F,a,b)
print('Squad = ',S,' Погрешность =' ,Err)

[S,N]=INT_Count(Pr,F,a,b,eps,nmax)
print('Sпр = ',S,' N = ',N)

[S,N]=INT_Count(Tr,F,a,b,eps,nmax)
print('Sтр = ',S,' N = ',N)

[S,N]=INT_Count(Simps,F,a,b,eps,nmax)
print('Sсимпс = ',S,' N = ',N)