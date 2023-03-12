def test():
    n = int(input())
    nums = list(map(int,input().split()))
    count = 0
    for i in nums:
        if i != 1:
            cnt = 0
            for j in range(2, round(i ** 0.5) + 1):
                if i % j == 0:
                    cnt += 1
            if cnt == 0:
                count += 1
    print(count)
    
    return
test()

