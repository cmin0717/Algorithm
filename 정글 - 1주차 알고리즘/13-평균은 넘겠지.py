def test():
    n = int(input())

    for i in range(n):
        m = list(map(int,input().split()))
        average = sum(m[1:]) / m[0]
        cnt = 0
        for j in m[1:]:
            if j > average: cnt +=1
        print("{:.3f}%".format(cnt/m[0]*100))

    return
test()


