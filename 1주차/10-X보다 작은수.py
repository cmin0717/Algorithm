def test():
    n,m = map(int, input().split())
    nums = list(map(int,input().split()))

    for i in nums:
        if i < m :print(i, end=' ')

    return

test()
