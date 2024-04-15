import heapq

n, m = map(int,input().split())
array = list(map(int, input().split()))
prique = []
for num in array:
    heapq.heappush(prique,-num)

for _ in range(n):
    max_val = heapq.heappop(prique)
    max_val += 1
    heapq.heappush(prique, max_val)

print(prique[0])