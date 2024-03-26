x = int(input())
list1 = []
for i in range(x):
    list1.append(input())
for i in range(x):
    result = oct(int(list1[i],16))
    print(result[2:])
