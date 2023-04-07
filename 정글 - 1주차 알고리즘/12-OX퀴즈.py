def test():
    n = int(input())

    for i in range(n):
        ox = input()
        point = 0
        cnt = 1
        for j in ox:
            if j == 'O':
                point += cnt
                cnt += 1
            else:
                cnt = 1
        print(point)

    return
test()