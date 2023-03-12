import sys
input = sys.stdin.readline

n = int(input())

table = [list(map(int,input().split())) for _ in range(n**2)]
classroom = [[0] * (n) for _ in range(n)]

def case1(idx): # 1단계 조건 : 빈칸중 좋아하는 학생이 제일 많이 인접한 칸
    find = table[idx][1:]
    send_arr = []
    m = 0
    for i in range(n):
        for j in range(n):
            r_num = classroom[i][j]
            if r_num == 0:
                cnt = 0
                for x,y in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
                    if 0 <= x < n and 0 <= y < n:
                        if classroom[x][y] in find:
                            cnt += 1
                m = max(m, cnt)
                send_arr.append([i,j,cnt])
    send_arr = [i for i in send_arr if i[-1] == m]
    return send_arr

def case2(arr): # 1단계에서 받은 좌표중 인접한 칸이 제일 많은 칸
    m = 0
    for idx in range(len(arr)):
        i = arr[idx][0]
        j = arr[idx][1]
        cnt = 0
        for x,y in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
            if 0 <= x < n and 0 <= y < n and classroom[x][y] == 0:
                cnt += 1
        arr[idx][-1] = cnt
        m = max(m, cnt)
    send_arr = [i for i in arr if i[-1] == m]
    return send_arr

def case3(arr): # 2단계에서 받은 좌표에서 가장 왼쪽 위에 있는 좌표
    arr.sort(key=lambda x:(x[0],x[1]))

    return arr[0][0],arr[0][1]

def result(classroom): # 완성된 자리의 점수 합산
    table.sort(key=lambda x:x[0])
    total = 0
    point = [0,1,10,100,1000]
    for i in range(n):
        for j in range(n):
            num = classroom[i][j]
            cnt = 0
            for x,y in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
                if 0 <= x < n and 0 <= y < n:
                    if classroom[x][y] in table[num-1][1:]:
                        cnt += 1
            total += point[cnt]
    return total

for i in range(n**2):
    # 각 단계별로 진행하였다.
    arr = case1(i)
    arr2 = case2(arr)
    x,y = case3(arr2)
    classroom[x][y] = table[i][0]

print(result(classroom))