import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

room = [i for i in range(n+1)]

villain = sorted([list(map(int,input().split())) for _ in range(m)]) # 벽을 정렬된 상태로 시작해야하니깐 정렬시킴

for x,y in villain: # x,y을 받아와서 시작점 방번호로 시작한다.
    num = room[x]
    for i in range(x,y+1):
        room[i] = num

print(len(set(room[1:]))) # set자료형을 이용하여 중복값 삭제