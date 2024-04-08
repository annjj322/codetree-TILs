n, m = map(int,input().split())
dictionary = dict()

for i in range(n):
    i += 1
    dictionary[input()] = i

for _ in range(m):
    test = input()
    if test not in dictionary:
        for k, v in dictionary.items():
            if v == int(test):
                print(k)
    else:
        print(dictionary[test])