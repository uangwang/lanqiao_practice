arr = []
#最大的面值是2023+2023=4046
for i in range(0,4047):
    arr.insert(i,0)
# print(arr)
for i in range(1,2024):
    for j in range(i+1,2024):
        arr[i+j] += i
print(max(arr))