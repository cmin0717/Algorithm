def test():
    n = int(input())

    def check(n):
        if n == 1:
            return False
        else:
            for i in range(2,int(n**0.5)+1):
                if n % i ==0:
                    return False
            return True

    for i in range(n):
        num = int(input())
        mid_num = num // 2
        
        for j in range(mid_num,1,-1):
            if check(j) and check(num-j):
                print(j,num-j)
                break

test()