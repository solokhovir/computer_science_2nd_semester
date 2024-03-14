f = open('6-6.txt', 'r')
line = f.read()
X = []

for x in line.split():
    X.append(int(x))

print('Исходный массив X')
print(X)

N = len(X)
Y = []

for i in range(N):
    if X[i] > 0:
        Y.append(X[i])

for i in range(N):
    if X[i] < 0:
        Y.append(X[i])

print('Новый массив Y')
print(Y)
f.close()