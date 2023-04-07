def test():
    n = int(input())
    def hanoi(n,x,y,z):
        if n == 1: # 남은 원판이 1개일 경우에는 1 -> 3으로 이동해야함으로 x,z
            print(x,z)
            return
        else: # 남은 원판이 1개가 아닐경우
            hanoi(n-1,x,z,y) # 원판하나를 1 -> 2로 이동후
            print(x,z)  # 1 -> 3으로 이동후
            hanoi(n-1,y,x,z) # 2에 있던 원판을 2 -> 3으로 이동
            # 이렇게 재귀적으로 반복해준다.
    if n > 20 :
        print((2**n)-1)
    else:
        print((2**n)-1)
        hanoi(n,1,2,3)
    return

test()
