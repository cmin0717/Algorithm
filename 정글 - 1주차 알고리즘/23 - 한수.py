def test():
    num = int(input())
    if num < 100:
        print(num)
    else:
        cnt = 99
        for i in range(100,num+1):
            a = str(i)[0]
            b = str(i)[1]
            c = str(i)[2]
            if int(b) * 2 == int(a) + int(c):
                cnt += 1
        print(cnt)
    return
test()
