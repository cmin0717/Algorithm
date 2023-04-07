def test():
    n = int(input())

    for i in range(n):
        a,b = input().split()
        result = ''
        for j in b:
            result += j*int(a)
        print(result)
    return
    
test()