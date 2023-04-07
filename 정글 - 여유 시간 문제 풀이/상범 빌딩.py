from collections import deque
import sys
input = sys.stdin.readline

while True:
    high,col,row = map(int,input().split())

    if high+col+row == 0: # 입력값이 다 0이면 종료
        break

    building = [[] for _ in range(high)] # 3중 리스트를 이용하기위해 미리 층에 해당하는 리스트 만듬
    q = deque()

    for i in range(high):
        for j in range(col):
            n = ','.join(input().rstrip()).split(',') # 문자열로 입력 받으면 값을 바꾸기 힘드니 리스트로 변환
            building[i].append(n)
            if 'E' in n: # 상범이의 위치를 큐에 담는다.
                q.append([i,j,n.index('E'),0])
                building[i][j][n.index('E')] = '#' # 미리 방문 체크해둔다.
        input() # 각 층입력후 빈칸이 입력되기에 입력만 받는다.

    time = 0
    while q:
        h,l,w,t = q.popleft()

        if building[h][l][w] == 'S': # 만일 출구가 나왔다면 현재까지 시간 출력
            print(f"Escaped in {t} minute(s).")
            break
        
        # 조건에 맞게 진행한다.
        for x,y,z in [h,l,w+1],[h,l,w-1],[h,l+1,w],[h,l-1,w],[h-1,l,w],[h+1,l,w]:
            if 0 <= x < high and 0 <= y < col and 0 <= z < row and building[x][y][z] != '#':
                q.append([x,y,z,t+1])
                if building[x][y][z] != 'S':
                    building[x][y][z] = '#'
    else:
        # break문을 만나지 못했다면 출구를 못찾은것!
        print("Trapped!")


