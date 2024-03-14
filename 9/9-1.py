# Метод итераций

import math
import numpy as np

N = 3

A = np.genfromtxt('9A.txt')
print('Исходный массив A')
print(A)

B = np.genfromtxt('9B.txt')
print('Исходный массив B')
print(B)

Adiag = np.diag(A)
Alpha = A.T/Adiag
Alpha[np.diag_indices_from(Alpha)] = 0
Alpha = Alpha.T

print('===================')
print(Alpha)
print('===================')

Beta = B/Adiag
print(Beta)
print('===================')

x1 = np.zeros(N, dtype = float)
x = Beta
KMAX = 100
k = 0

while(np.max(abs(x-x1))>0.001) & (k<KMAX):
    x = x1
    x1 = Beta - np.dot(Alpha,x)
    k += 1

print("k = ",k, "Погрешность = ", np.max(abs(x-x1)))

print('')
print('X')

for i in range (0,N):
    print('%f'%x1[i],end=' ')
print('')