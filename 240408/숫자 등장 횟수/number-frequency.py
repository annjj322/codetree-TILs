n, m = map(int,input().split())
n_array = list(map(int,input().split()))
m_array = list(map(int,input().split()))
counter = dict()

for num in n_array:
    if num not in counter:
        counter[num] = 1
    else:
        counter[num] += 1

for num in m_array:
    if num not in counter:
        print(0,end=' ')
    else:
        print(counter[num],end=' ')