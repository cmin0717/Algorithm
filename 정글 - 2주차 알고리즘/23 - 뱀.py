import sys
from collections import deque
input = sys.stdin.readline

n = int(input())  # 지도의 크기 입력

apple_cnt = int(input())
apple = deque([list(map(int,input().split())) for _ in range(apple_cnt)]) # apple 좌표를 deque에 받는다. 애플을 먹을경우 바로 지워주기 위해

direction_cnt = int(input())
direction = deque([list(input().rstrip().split()) for _ in range(direction_cnt)]) # 이것도 deque받아 사용했다면 바로 지워주자

snake = deque() # 뱀이 있는 좌표를 계속 넣고 지운다.
snake.append([1,1]) # 뱀이 출발하는 좌표는 1,1 고정이므로 미리 넣어준다.
cnt = 0 # 매초 저장

dx = [0,1,0,-1] # 방향을 바꿀경우 이용
dy = [1,0,-1,0]
dir = 0 # 현재 가는 방향을 설정

def left(m):
    if m == 0: # 인덱스를 넘어가기 때문에 다시 설정
        m = 4
    return m - 1
def right(m): # 위와 동일
    if m == 3:
        m = -1
    return m + 1

while True:
    cnt += 1 # 시간 추가

    if snake[-1][0] < 1 or snake[-1][0] > n or snake[-1][1] < 1 or snake[-1][1] > n: # 만약 판을 넘어갔다면 끝!
        cnt -= 1 # 끝이기 떄문에 위에서 더해준 시간을 1초 다시 뺸다.
        break

    if [snake[-1][0]+dx[dir], snake[-1][1]+dy[dir]] in apple: # 새로 이동한 좌표에 사과가 있다면
        snake.append([snake[-1][0]+dx[dir], snake[-1][1]+dy[dir]]) # snake에 추가만 하고 pop은 하지 않는다.
        apple.remove(snake[-1]) # 먹은 사과는 삭제
    else:
        snake.append([snake[-1][0]+dx[dir], snake[-1][1]+dy[dir]]) # 사과를 먹지 않았다면 추가 후 꼬리쪽 삭제
        if snake.count(snake[-1]) > 1: # 만일 같은 좌표가 2개가 있다면 뱀이 자기 자신한테 가로막힌 거니깐 끝!
            break 
        snake.popleft() # 꼬리 삭제

    for i,j in direction: # 입력 받은 방향을 for문을 통해 돌리고 만일 cnt가 맞는게 있다면 방향 재설정
        if cnt == int(i):
            direction.popleft()
            if j == 'D':
                dir = right(dir)
                break
            else:
                dir = left(dir)
                break
print(cnt)
