def test():
    A,B = map(int, input().split())
    a = A+B
    b = A-B
    c = A*B
    d = A//B
    e = A%B
    print(a,b,c,d,e,end='\n')
test()