n = 4
array = []
for i in range(n):
    array.append(input().split())
sum = 0

for i in range(n):
    for j in range(n):
        sum += int(array[i][j])
    print(sum)
    sum = 0