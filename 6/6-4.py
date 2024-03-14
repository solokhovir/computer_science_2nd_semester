print('----1 способ----')
f = open('6-4.txt', 'r')
line = f.read()
X = []

for x in line.split():
    X.append(int(x))

print('Исходный массив X')
print(X)

N = len(X)
R = X[0]
k = 0

for i in range(N):
    if X[i]>R:
        R = X[i]
        k = i

print('X[%d] = %f'%(k,R))
f.close()

# 2й способ
R = max(X)
k = X.index(R)

print('----2 способ----')
print('X[%d] = %f'%(k,R))