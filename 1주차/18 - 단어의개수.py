def test():
    s = input()
    cnt = 0
    for i in s.split(' '):
        if i != '':cnt +=1
    print(cnt)
    return
test()

# def test():
#     n = input().split()
#     print(len(n))
#     return
# test()