f = open('6-7.txt', 'r')
line = f.read()
X = []

for x in line.split():
    X.append(int(x))

print('Исходный массив X')
print(X)

N = len(X)

for i in range(0,N,2):
    X[i] *= 2
for i in range(1,N,2):
    X[i] = 0

print('Новый массив X')
print(X)
f.close()