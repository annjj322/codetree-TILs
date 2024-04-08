n, m = map(int,input().split())
dictionary = dict()
rev_dict = dict()

for i in range(n):
    i += 1
    train = input()
    dictionary[train] = i
    rev_dict[i] = train

for _ in range(m):
    test = input()
    if test not in dictionary:
        print(rev_dict[int(test)])
    else:
        print(dictionary[test])