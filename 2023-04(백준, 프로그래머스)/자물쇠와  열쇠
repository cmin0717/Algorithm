def solution(key, lock):
    m,n = len(lock),len(key)
    new_lock = [[0] * (m*3) for _ in range(m*3)] # 자물쇠에 패딩을 입혀준다.

    # 가운데에는 실제 자물쇠 값 입력
    for i in range(m):
        for j in range(m):
            new_lock[i+m][j+m] = lock[i][j]
    
    # 키로 자물쇠를 열었는지 확인하는 함수
    def check():
        for i in range(m,m*2):
            for j in range(m,m*2):
                if new_lock[i][j] == 0:
                    return False
        return True
    
    # 키의 값을 시계방향으로 90도 회전한 값을 새로운 키값에 저장
    def change(k):
        new_k = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                x = j
                y = n-i-1
                new_k[x][y] = k[i][j]
        return new_k
    
    # 4가지의 방향에대한 키를 확인
    for k in range(4):
        if k != 0:
            key = change(key)
        # 패딩준 자물쇠 확인
        for i in range(m*3-n):
            for j in range(m*3-n):
                temp = True
                visit = []
                # 키 대입
                for x in range(n):
                    for y in range(n):
                        if key[x][y] == 1 and new_lock[x+i][y+j] == 1:
                            temp = False
                            break
                        if key[x][y] == 1 and new_lock[x+i][y+j] == 0:
                            new_lock[x+i][y+j] = 1
                            visit.append([x+i,y+j])
                    if not temp:
                        break
                # 만약 키와 자물쇠가 충돌이 없었다면 열렸는지 확인
                if temp:
                    if check():
                        return True
                # 체크한 부분들 원상복구
                for x,y in visit:
                    new_lock[x][y] = 0
    # 한번도 열지 못했다면 false 출력
    return False

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])