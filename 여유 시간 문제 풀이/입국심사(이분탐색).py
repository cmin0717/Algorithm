import sys
input = sys.stdin.readline

n,m = map(int,input().split())

time = [int(input()) for _ in range(n)]

start,end = 0,max(time)*m # 시작점과 끝점을 정한다.

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in time: # 각 심사대에서 해당 시간에 처리할수있는 손님을 더해준다.
        count += mid // i
    if count >= m: # 손님이 m값보다 크다면 end를 변경
        end = mid -1
    else:
        start = mid + 1
print(start)