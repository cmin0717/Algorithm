import sys
input = sys.stdin.readline

n, L, R = map(int,input().split())
country = [list(map(int,input().split())) for _ in range(n)]

# 해당 나라에서 이동할 수 있는 다른 나라를 구하는 함수
def func(i,j):
    global people

    check = [[i,j]] # 초기값으로 자기 자신을 넣어준다.
    conn_ct = []

    while check:
        x,y = check.pop()
        for a,b in [x+1, y],[x-1, y],[x, y+1],[x,y-1]:
            if 0 <= a < n and 0 <= b < n and visit[a][b] == 0:
                c = abs(country[x][y] - country[a][b]) 
                if L <= c <= R:
                    # 각 조건에 다 만족한다면
                    people += country[a][b] # 이동할 수 있는 총 인구를 구하기 위해
                    visit[a][b] = 1 # 중복 방문을 막기위해
                    check.append([a,b])
                    conn_ct.append([a,b]) # 연결되 나라를 찾기 쉽게 리스트에 넣어둔다.
    if conn_ct: # 만약 연결된 나라가 있다면 인덱스 -1값에 이동 가능 총 인구를 넣어준다.
        conn_ct.append(people)
    return conn_ct

time = 0 # 인구 이동 발생 총 일수
while True:
    move_ct = [] # 인구 이동이 가능한 나라들을 리스트에 담는다.
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                people = 0
                li = func(i,j)
                if li: # 현재 나라에서 인구 이동이 있는 나라가 있는 경우
                    move_ct.append(li)
    if move_ct: # 인구이동 가능 나라가 있는경우
        time += 1        
        for i in range(len(move_ct)):
            new_people = move_ct[i][-1] // (len(move_ct[i])-1)
            for x,y in move_ct[i][:-1]:
                country[x][y] = new_people 
    else: # 없는 경우 더이상 확인 X
        print(time)
        break
