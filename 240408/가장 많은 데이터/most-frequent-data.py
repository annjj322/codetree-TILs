n = int(input())
main_dict = dict()

for _ in range(n):
    color = input()
    if color not in main_dict:
        main_dict[color] = 1
    else:
        main_dict[color] += 1

print(max(main_dict.values()))