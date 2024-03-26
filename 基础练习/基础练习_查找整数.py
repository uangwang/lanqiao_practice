n = int(input())

num_list = input().split()
search_num = input()

if search_num in num_list:
    print(num_list.index(search_num) + 1)
else:
    print(-1)
