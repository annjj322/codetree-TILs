n = int(input())
n_array = []
for i in range(n):
    n_array.append(list(map(int,input().split())))

sum_array = []
sum = 0

for row in range(len(n_array)-2):
    for col in range(len(n_array[0])-2):
        for i in range(3):
            for j in range(3):
                sum += n_array[i+row][j+col]
        sum_array.append(sum)
        sum = 0
print(max(sum_array))