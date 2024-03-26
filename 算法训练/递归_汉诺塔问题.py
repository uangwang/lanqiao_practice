# N个盘子从A移动到C，借助B
def Move(n,A,B,C):
    if n==1:
        print(A,'-->',C)
    else:
        # 将n-1个盘子从A移动到B，借助C
        Move(n-1,A,C,B)
        # 将第n个盘子从A移动到C
        Move(1,A,B,C)
        # 将n-1个盘子从B移动到C，借助A
        Move(n-1,B,A,C)

if __name__ == '__main__':
    Move(3,'A','B','C')