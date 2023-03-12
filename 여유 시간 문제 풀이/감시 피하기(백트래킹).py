import sys
input = sys.stdin.readline

n = int(input())
std = {'T' : 1, 'S' : -6, "X" : 0} # 덧셈으로 하려고 했는데 의미없는짓을 했다...
teacher = []
classroom = []

for i in range(n):
    line = list(map(lambda x : std[x], input().rstrip().split()))
    classroom.append(line)
    for j in range(n):
        if line[j] == 1:
            teacher.append([i,j]) # 선생의 좌표를 저장

def check(arr): # 조건에 만족하는지 체크하는 함수
    for x,y in arr:
        y_line = [classroom[i][y] for i in range(n)]

        for list in classroom[x][:y][::-1],classroom[x][y:],y_line[:x][::-1],y_line[x:]:
            count = 0
            for j in list:
                count += j
                if count < 0: # count가 음수라면 학생과 선생사이의 장애물이 없다는 뜻
                    return False
    return True

def run(cnt):
    if cnt == 3: # 장애물이 3개면 조건을 체크
        if check(teacher):
            print('YES')
            exit() # 조건에 만족하면 바로 종료
        else:
            return
    for i in range(n):
        for j in range(n):
            if classroom[i][j] == 0:
                classroom[i][j] = 30
                run(cnt+1)
                classroom[i][j] = 0
run(0)
print('NO') # 종료되지 않고 여기까지 왔다면 조건을 만족하는 경우가 없을 경우다.