n = int(input())
dictionary = dict()
cmd_list = []

for _ in range(n):
    cmd_list.append(list(map(str,input().split())))
for cmd in cmd_list:
    if cmd[0] == 'add':
        dictionary[cmd[1]] = cmd[2]
    elif cmd[0] == 'find':
        if cmd[1] not in dictionary:
            print(None)
        else:
            print(dictionary[cmd[1]])
    elif cmd[0] == 'remove':
        dictionary.pop(cmd[1])