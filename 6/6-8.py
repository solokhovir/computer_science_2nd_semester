f = open('6-8.txt', 'r')
line = f.read()
X = []

for x in line.split():
    X.append(int(x))

print('Исходный массив X')
print(X)

X.reverse()
print('Новый массив X')
print(X)

f.close()