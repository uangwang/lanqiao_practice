n = int(input())
num_list = list(map(int, input().split()))

for i in range(n - 1):
    min_value = num_list[i]
    min_indx = i
    for j in range(i, n):
        if num_list[j] < min_value:
            min_value = num_list[j]
            min_indx = j

    num_list[min_indx], num_list[i] = num_list[i], num_list[min_indx]

print(" ".join(map(str, num_list)))