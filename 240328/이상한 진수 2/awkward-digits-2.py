n = input()
array = []
binary = bin(int(n,2))
for num in binary[2:]:
    array.append(num)

if '0' not in array:
    array[-1] = '0'
else:
    for i in range(len(array)):
        if array[i] == '0':
            array[i] = '1'
            break
    

result = ''.join(map(str,array))
print(int(result,2))