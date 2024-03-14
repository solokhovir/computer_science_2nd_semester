f = open('6-2.txt', 'r')
line = f.read()
A = []

for x in line.split():
    A.append(int(x))

print('Исходный массив A')
print(A)

N = len(A)
s = 0
k = 0

for i in range(N):
    if A[i]>0:
        s += A[i]
        k += 1

if k > 0:
    s /= k

print('s = %f'%s)
f.close()