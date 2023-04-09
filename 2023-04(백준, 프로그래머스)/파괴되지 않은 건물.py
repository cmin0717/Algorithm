def solution(board, skill):
    n,m = len(board), len(board[0])
    check = [[0]*m for _ in range(n)] # 누적합을 사용하기 위해 선언

    for s in skill:
        t,r1,c1,r2,c2,d = s
        if t == 1: # 공격이면 값을 -로 변환
            d = -d
        # 누적합을 사용하기위해(왼쪽에서 오른쪽으로 누적합하고 위에서 아래로 누적합을 사용할것이다.)
        # 그러면 범위가 주어졌을때 왼쪽 시작점에만 값을 넣어주고 끝나는점에는 빼주는 값을 넣어준다면 연산을 4번만하면 된다.
        check[r1][c1] += d # 왼쪽시작점
        if c2+1 < m:
            check[r1][c2+1] -= d # 행의 오른쪽 끝점
        if r2+1 < n:
            check[r2+1][c1] -= d # 열의 왼쪽 끝점
        if r2+1 < n and c2+1 < m:
            check[r2+1][c2+1] += d # 마지막 열의 오른쪽 끝점

    # 행의 누적합
    for i in range(n):
        for j in range(1,m):
            check[i][j] += check[i][j-1]
    # 열의 누적합
    for i in range(1,n):
        for j in range(m):
            check[i][j] += check[i-1][j]
    
    # 결과 추출
    result = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + check[i][j] > 0:
                result += 1
    return result
# 누적합을 생각하지 못했다. 사람들 너무 똑똑한듯....