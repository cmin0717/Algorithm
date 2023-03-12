import sys
input = sys.stdin.readline

n = int(input())
cost = list(map(int,input().split()))
total = int(input())
max_cost = max(cost)

if sum(cost) <= total: # 원하는 예산을 다 줘도 남을때는 가장 큰 예산 출력
    print(max_cost)
else:
    start,end = 0, max_cost # 시작점과 끝점 설정
    while start <= end:
        check_cost = 0
        mid = (start+end) // 2

        for num in cost:
            if num > mid:
                check_cost += mid
            else:
                check_cost += num
        
        if check_cost <= total:
            start = mid +1
        else:
            end = mid - 1
    print(end)

    

