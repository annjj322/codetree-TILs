n,m = map(int, input().split())
saved_num = 1
for i in range(100,0,-1):
    if n % i == 0 and m % i == 0:
        n = n/i
        m = m/i
        saved_num *= i

print(int(saved_num*n*m))