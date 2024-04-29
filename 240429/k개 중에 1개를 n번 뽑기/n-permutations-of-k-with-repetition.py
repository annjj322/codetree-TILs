k, n = map(int,input().split())
answer = []

def printer():
    for elem in answer:
        print(elem, end = " ")
    print()

def choose(curr_num):
    # print when curr_num is max
    if curr_num == n+1:
        printer()
        return

    for i in range(1,k+1):
        answer.append(i) # in
        choose(curr_num+1)
        answer.pop() # out

    return

choose(1)