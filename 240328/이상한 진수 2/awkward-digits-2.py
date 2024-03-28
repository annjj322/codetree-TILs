n = input()
array = []
binary = bin(int(n,2))
for num in binary[2:]:
    array.append(num)

for i in range(len(array)):
    if array[i] == '0':
        print(array[i])
        array[i] = '1'
        break
result = ''.join(map(str,array))
print(int(result,2))