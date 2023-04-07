import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())
rest = [0] + list(map(int,input().split())) + [l] # 고속도로 시작점과 끝점 패딩
rest.sort() # 이분 탐색을 위해 정렬

start,end = 1, l # 시작점과 끝점을 설정

while start <= end:
    mid = (start+end)//2
    count = 0

    for i in range(1,n+2): # 시작점과 끝점을 추가했으니 n+2만큼 확인해야한다.
        if rest[i] - rest[i-1] > mid:
            count += (rest[i] - rest[i-1] -1) // mid # 나머지가 0일경우는 설치가 불가하니깐 -1로 구별한다.

    if count > m:
        start = mid + 1
    else:
        end = mid - 1
print(start)