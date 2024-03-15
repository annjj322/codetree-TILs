def main():
    y, m, d = map(int,input().split())
    yoon = False
    long_month = [1,3,5,7,8,10,12]
    short_month = [4,6,9,11]
    spring = [3,4,5]
    summer = [6,7,8]
    fall = [9,10,11]
    winter = [12,1,2]
    if m in long_month:
        if d > 31:
            print(-1)
            return
    elif m in short_month:
        if d > 30:
            print(-1)
            return
    elif y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                yoon = True
        else:
            yoon = True

    if yoon == False and m == 2 and d > 28:
        print(-1)
        return
    else:
        if m in spring:
            print("Spring")
        elif m in summer:
            print("Sumemr")
        elif m in fall:
            print("Fall")
        elif m in winter:
            print("Winter")

main()