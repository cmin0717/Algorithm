def test():
    a,b,v = map(int,input().split())

    n = (v - a) // (a - b)
    if (v - a) % (a - b) == 0 :
        print(n+1)
    else:
        print(n+2)
    
    return

test()
