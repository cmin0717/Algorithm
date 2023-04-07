def test():
    nums = []
    for i in range(9):
        num = int(input())
        nums.append(num)
    print(max(nums),nums.index(max(nums))+1,sep='\n')
    return

test()

def test():
    a = 0
    b = 0
    for i in range(1,10):
        num = int(input())
        if a < num :
            a = num
            b = i
    print(a,b, sep='\n')

    return

test()