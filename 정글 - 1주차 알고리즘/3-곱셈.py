def test():
    n = input()
    m = input()
    for i in range(2,-1,-1):
        a = int(m[i])*int(n)
        print(a)
    print(int(n)*int(m))

test()