a, b = map(int,input().split())

def calc(a,b):
    if a < b :
        a += 10
        b *= 2
    else:
        a *= 2
        b += 10
    return a, b

result_a, result_b = calc(a,b)
print(result_a, end = ' ')
print(result_b)