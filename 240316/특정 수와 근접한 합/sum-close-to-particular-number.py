n,s = map(int,input().split())
sum_array = []
n_array = list(map(int,input().split()))
n_array.sort()

for i in range(len(n_array)):
    tmp1_array = n_array[:i] + n_array[i+1:]
    for j in range(len(n_array)-1):
        tmp2_array = tmp1_array[:j] + tmp1_array[j+1:]
        sum_array.append(sum(tmp2_array))
minus_array = []
for num in sum_array:    
    minus_array.append(abs(num-s))
print(min(minus_array))