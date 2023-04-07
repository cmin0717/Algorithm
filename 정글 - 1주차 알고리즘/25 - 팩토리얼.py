def test():
    n = int(input())

    def fac(m):
        if m == 0:
            return 1
        else:
            return m * fac(m-1)

    print(fac(n))
    return
test()


def test():
    n = int(input())
    m = 1
    for i in range(n,0,-1):
        m = m * i
    print(m)
    return
test()