n, h, t = map(int,input().split())
if t > n:
    t = n
elif t > 10:
    t = 10

array_n = list(map(int,input().split()))
minus_array = []
for num in array_n:
    minus_array.append(abs(num-h))
sum_array = []
tmp = 0
for j in range(len(minus_array)-t+1):
    for i in range(t):
        tmp += minus_array[i+j]
    sum_array.append(tmp)
    tmp = 0
print(min(sum_array))