n, m = map(int,input().split())
n_array = list(map(int,input().split()))
m_array = list(map(int,input().split()))

for num in m_array:
    print(n_array.count(num), end = ' ')