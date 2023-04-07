def test():
    x,y,w,h = map(int,input().split())

    nums = [w-x, x, h-y, y]

    print(min(nums))

    return

test()