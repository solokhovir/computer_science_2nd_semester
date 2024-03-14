f = open('6-5.txt', 'r')
line = f.read()
X = []

for x in line.split():
    X.append(int(x))

print('Исходный массив X')
print(X)

N = len(X)
R = 1e25
k = -1

for i in range(N):
    if X[i]<=0:
        continue
    if X[i]<R:
        R=X[i]
        k=i

if k==-1:
    print ('Нет положительных элементов')
else:
    print ('X[%d] = %f'%(k,R))

f.close()