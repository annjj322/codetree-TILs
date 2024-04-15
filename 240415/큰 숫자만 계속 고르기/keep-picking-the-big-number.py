import heapq

n, m = map(int,input().split())
array = list(map(int, input().split()))
prique = []
for num in array:
    heapq.heappush(prique,-num)

for _ in range(n):
    prique[0] += 1
    print(prique)