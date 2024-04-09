import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items, -item)
    
    def empty(self):
        return int(not self.items)
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        
        return -heapq.heappop(self.items)
    
    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        
        return -self.items[0]

n = int(input())
queue = PriorityQueue()
for _ in range(n):
    tmp = list(map(str,input().split()))
    if len(tmp) == 2:
        queue.push(int(tmp[1]))
    else:
        if tmp[0] == 'size':
            print(queue.size())
        elif tmp[0] == 'pop':
            print(queue.pop())
        elif tmp[0] == 'empty':
            print(queue.empty())
        elif tmp[0] == 'top':
            print(queue.top())