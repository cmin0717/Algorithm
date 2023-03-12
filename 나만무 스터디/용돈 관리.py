import sys
input = sys.stdin.readline

n, m = map(int,input().split())

money = [int(input()) for _ in range(n)]

start = max(money) # 최소가지고 있어야 하는 돈이 하루의 최대 지출보다는 커야한다.
end = sum(money) 

while start < end:
    mid = (start + end) // 2

    cnt = 0
    check = 0
    for i in money:
        check += i
        if check > mid:
            cnt += 1
            check = i
        if cnt > m:
            break
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(start)

