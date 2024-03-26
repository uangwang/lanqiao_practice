n = int(input()) # 部落的数量
a = list(map(int, input().split())) # 每个部落的人数
# 转换为堆，因为堆每次都能取到最小值，或者添加元素
import heapq
heapq.heapify(a)
ans = 0
while len(a) >= 2:
    # 每次取出两个最小的元素，合并为一个元素
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    # 将合并后的元素放回堆中
    heapq.heappush(a, x+y)
    ans += x+y
print(ans)

