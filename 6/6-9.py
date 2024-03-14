f=open('6-8A.txt', 'r')
line = f.read()
A=[]

for x in line.split():
    A.append(int(x))

print('Исходный массив A')
print(A)

N=len(A)
f.close()

f=open('6-8B.txt', 'r')
line = f.read()
B=[]

for x in line.split():
    B.append(int(x))

print('Исходный массив B')
print(B)

M=len(B)
f.close()
N=min(N,M)
C=[]

for i in range(0,N):
    C.append(A[i])
    C.append(B[i])

print('Новый массив C')
print(C)