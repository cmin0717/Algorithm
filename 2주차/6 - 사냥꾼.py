import sys
input = sys.stdin.readline

m,n,r = map(int, input().split())

arr = list(map(int,input().split())) # 사냥꾼들의 위치 저장
arr.sort() # 이분 탐색을 위한 정렬
animal = [list(map(int,input().split())) for _ in range(n)] # 동물들 위치 저장

hunt_cnt = 0

for i in animal:
    # if i[1] > r: # 이 조건문이 없는게 조금더 빠르게 나온다. 이유는 모르겠다.
    #     continue
    start, end = 0, m-1 # 시작점을 0 끝점을 사냥꾼의 리스트 마지막 인덱스
    while start <= end:
        mid = (start + end) // 2
        if abs(arr[mid] - i[0]) + i[1] <= r: # 현재 위치에서 해당 동물을 잡을수 있다면 hunt_cnt += 1해주고 break
            hunt_cnt += 1
            break
        elif i[0] > arr[mid]: # 현재 사냥꾼보다 오른쪽 사냥꾼들이 잡아야한다면 start점을 변경
            start = mid +1
        else:
            end = mid -1 # 왼쪽 사냥꾼이 잡아야한다면 end점 변경
                
print(hunt_cnt)
