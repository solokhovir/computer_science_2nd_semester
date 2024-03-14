f = open('6-1.txt', 'r')
line = f.read()
a = []

for x in line.split():
    a.append(int(x))

print('Исходный массив A')
print(a)

N = len(a)
s = 0

for i in range(N):
    s += a[i]

print('s =', s)

f.close()