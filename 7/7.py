import numpy as np

A=np.genfromtxt('LinalgA.txt')

print('Исходный массив A')
print(A)

B=np.genfromtxt('LinalgB.txt')
print('Исходный массив B')
print(B)

P=np.genfromtxt('LinalgP.txt')
print('Исходный массив P')
print(P)

Q=np.genfromtxt('LinalgQ.txt')
print('Исходный массив Q')
print(Q)

R=np.genfromtxt('LinalgR.txt')
print('Исходный массив R')
print(R)

x = np.dot(B,P)
print ('x =', x)

y = np.dot(A,x)
print ('y =', y)

z = y+Q
print ('z =', z)
s = np.dot(z,R)
print ('s =', s)