import numpy as np

N = 3
A = np.genfromtxt('10.txt')

print('Исходный массив A')
print(A)
print('Исходный массив A')

for i in range (0,N):
    for j in range (0,N):
        print('%f'%A[i][j], end=' ')
    print('')

L, X = np.linalg.eig(A)

print('Собственные значения A')
print(L)
print('Собственные векторы A')

for i in range (0,N):
    for j in range (0,N):
        print('%f'%X[i][j], end=' ')
    print('')