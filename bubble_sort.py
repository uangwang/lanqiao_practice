def Bubble_sort(a,length):
    for i in range(length-1): # length-1次排序，不用自己和自己比
        ctn = 0
        for j in range(length-1-i): # 每次排序都会有一个最大值放在最后，所以每次排序都会少一个数
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                ctn += 1
                print(a)
    return a

if __name__ == '__main__':
    a = list(map(int, input().split()))
    length = len(a)
    print("排序前：",a)
    print("排序",Bubble_sort(a,length))