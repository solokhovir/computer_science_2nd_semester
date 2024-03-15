N = int(input("Введите N: "))
X = []

for i in range(0,5):
    x = float(input("Введите x: "))
    # print("type_x:", type(x))
    X.append(x)

#X=[0.1,0.3, 0.4, 0.7, 1]
print(' -------------------------')
print(' | x         |         s |')
print(' -------------------------')

for x in X:
    s = 0
    u = -x
    for k in range(1,N+1):
        s += u/k
    print(" | %8.4f | %8.4f |" % (x,s))

print(' -------------------------')