def fab(n):
    if(n==1 or n==2):
        return 1
    else:
        return fab(n-1) % 10007 + fab(n-2) % 10007

n = int(input())
print(fab(n))
