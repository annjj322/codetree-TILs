a, b, x, y = map(int, input().split())

case1 = abs(a-b) # a to b distance
case2 = abs(a-x) + abs(b-y) # a to x distance + b to y distance
case3 = abs(a-y) + abs(b-x) # a to y distance + b to x distance

case_array = [case1,case2,case3]
print(min(case_array))