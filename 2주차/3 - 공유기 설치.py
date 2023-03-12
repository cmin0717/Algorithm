import sys
input = sys.stdin.readline # 입력받는 수가 많기때문에 해주어야한다. 안했을 경우 시간 초과뜸

n,c = map(int, input().split())
house = [int(input()) for _ in range(n)]

house.sort() # 이분 탐색을 위해 일단 집 리스트 정렬

start = 1 # 집 사이의 최소 거리
end = house[-1] - house[0] # 주어진 집사이의 최대거리

while start <= end: # 범위를 바꾸어 설치하다가 start값이 end값을 넘어가면 mid값 출력
    mid = (start + end) // 2 
    c_cnt = 1 # 공유기 설치 횟수
    start_home = house[0] # 공유기가 설치된 집의 좌표
    for i in range(1,n):
        if house[i] - start_home >= mid: # i위치의 집과 공유기가 설치된 집의 거리가 mid보다 크거나 같다면 그 위치에 공유기 설치
            c_cnt += 1
            start_home = house[i] # 새로운 공유기를 설치했으니깐 좌표 재설정
    if c_cnt >= c: # 설치된 공유기의 수가 같거나 크면 다시 범위를 넓혀 다시 설치
        start = mid + 1
    else:
        end = mid -1 # 공유기가 적게 설치 되었다면 범위를 줄여 다시 설치

print(end)

# 이해하는데 정말 오래걸렸던거 같다....결국 기준점을 잘 설정해서 조건에 맞추어 start,end값을 재설정하며 풀어가야한다.