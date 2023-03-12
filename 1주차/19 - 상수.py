def test():
    n,m = input().split()

    n = ''.join(reversed(n))
    m = ''.join(reversed(m))
    print(max(n,m))
    return

test()
