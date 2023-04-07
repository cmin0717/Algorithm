import sys
input = sys.stdin.readline

n,m = map(int,input().split())

pan = [[]for _ in range(n)]

for i in range(n): # 주어진 판을 작업하기 편하게 인덱스 별로 나누어서 리스트에 저장
    for word in input().rstrip():
        pan[i].append(word)

def cross_size(x,y): # 십자가가 존재한다면 제일 크게 존재하는 size를 반환

    cnt = [0]*4

    for i in range(y+1,m):
        if pan[x][i] == '*':
            cnt[0] += 1
        else:
            break
    if cnt[0] == 0: return 0 # cnt = 0이면 십자가가 존재 할수없으니 바로 리턴

    for i in range(y-1,-1,-1):
        if pan[x][i] == "*":
            cnt[1] += 1
        else:
            break
    if cnt[1] == 0: return 0

    for i in range(x-1,-1,-1):
        if pan[i][y] == "*":
            cnt[2] += 1
        else:
            break
    if cnt[2] == 0: return 0

    for i in range(x+1,n):
        if pan[i][y] == "*":
            cnt[3] += 1
        else:
            break
    
    return min(cnt)

result = []

for i in range(n):
    for j in range(m):
        if pan[i][j] == '*': # for문으로 돌다가 *을 만나면 cross_size를 확인
           size = cross_size(i,j)

           if size == 0: # size가 0이면 cross가 존재하지 않으니깐 패쓰
            continue

           for l in range(1,size+1): # 1 ~ size만큼 십자가를 추가 해준다.
            result.append([i+1,j+1,l])

for x,y,size in result: # 존재하는 십자가로 pan을 채울수 있나 확인하기 위해 십자가를 "."으로 다 변환
    x = x-1
    y = y-1
    pan[x][y] = '.'
    pan[x+size][y] = '.'
    pan[x-size][y] = '.'
    pan[x][y+size] = '.'
    pan[x][y-size] = '.'

for check in pan:
    if "*" in set(check): # pan을 돌면서 *가 나오면 십자가로 pan을 다 못채운거니깐 -1출력
        print(-1)
        break
else: # 위에서 break문을 만나지 않고 왔다면 십자가로 pan을 다 채운거니깐 십자가 수와 십자가 정보 출력
    print(len(result))
    for xy in result:
        print(*xy)

