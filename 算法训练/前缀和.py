def get_presum(a):
    n = len(a)
    sum = [0] * n
    sum[0] = a[0]
    for i in range(1,n):
        sum[i] = sum[i-1] + a[i]
    return sum

def get_sum(l,r,sum):
    if l ==0:
        return sum[r]
    else:
        return sum[r] - sum[l-1]

# print(get_presum([1,2,3,4,5]))
sum = get_presum([1,2,3,4,5])
print(sum)
print(get_sum(2,3,sum))