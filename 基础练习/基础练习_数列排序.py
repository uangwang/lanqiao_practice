a = input()
b = input()
c = []
c = b.split()

for i in range(0,int(a)):
    c[i] = int(c[i])

c = sorted(c)

for i in range(0,int(a)):
    print(c[i],end=" ")
