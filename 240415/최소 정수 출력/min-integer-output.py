import heapq

n = int(input())
x_queue = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(x_queue) == 0:
            print(0)
        else:
            result = heapq.heappop(x_queue)
            print(result)
    else:
        heapq.heappush(x_queue,num)