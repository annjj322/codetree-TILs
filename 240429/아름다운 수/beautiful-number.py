n = int(input())
answer = []
tmp_array = []

def choose(curr_num):
    if curr_num == n+1:
        tmp_array.append(0)
        return

    if n+1 - curr_num >= 4:
        for _ in range(4):
            answer.append(4)
            
        choose(curr_num+4)
        for _ in range(4):
            answer.pop()

    if n+1 - curr_num >= 3:
        for _ in range(3):
            answer.append(3)
        choose(curr_num+3)

        for _ in range(3):    
            answer.pop()

    if n+1 - curr_num >= 2:
        for _ in range(2):
            answer.append(2)
        choose(curr_num+2)
        for _ in range(2):
            answer.pop()
        
    answer.append(1)
    choose(curr_num+1)
    answer.pop()

    return

choose(1)
print(len(tmp_array))