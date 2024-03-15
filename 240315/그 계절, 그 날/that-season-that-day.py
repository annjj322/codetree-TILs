y, m, d = map(int,input().split())
yoon = False
long_month = [1,3,5,7,8,10,12]
short_month = [4,6,9,11]
spring = [3,4,5]
summer = [6,7,8]
fall = [9,10,11]
winter = [12,1,2]

if y % 4 == 0 and m == 2: # 윤년, 2월 체크
    if y % 100 == 0: # 100으로 나눠지면서
        if y % 400 == 0: # 동시에 400으로 나눠지면
            yoon = True # 윤년
    else:
        yoon = True # 100으로 안나눠지면 윤년

if yoon == False and m == 2 and d > 28:
    print(-1)
elif yoon == True and m == 2 and d > 29:
    print(-1)
elif m in long_month and d > 31:
    print(-1)
elif m in short_month and d > 30:
    print(-1)
else:
    if m in spring:
        print("Spring")
    elif m in summer:
        print("Summer")
    elif m in fall:
        print("Fall")
    elif m in winter:
        print("Winter")