f = open('6-3.txt', 'r')
line = f.read()
a = []

for x in line.split():
    a.append(int(x))

print('Исходный массив A')
print(a)

N = len(a)
p = 1

for i in range(N):
    if (a[i] == 0):
        break
    p *= a[i]

s = 0

for j in range(i + 1, N):
    s += a[j]

print('p =', p)
print('s =', s)
f.close()