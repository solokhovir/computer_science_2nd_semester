from math import *
k = 2
r = 2
x = 2
y = 1
r1 = abs(r)**(5*x*y) + tan(3*k)
print('r1=', r1)
x = 0.5
r2 = sqrt(log(x)**2+1)+3*x**(1/3)
print('r2=', r2)
x = 1.0
y = 2.0
z = 3.0
r3 = (x+3*y) / (2*z) - 3*abs(x)*exp(x+y) / (x+y) + 1 / (1 + 1 / (1 + 1/x))
print('r3=', r3)
x = 0.3
r4 = sin(x/2)**3 + cos(x**2) - 2*cos(3*x)**(1/5)
print('r4=', r4)