cnt_1, cnt_0 = 0, 0

# 분할정복 사용
def check(x,y,r,arr):
    global cnt_1, cnt_0

    # 기준점 설정
    standard = arr[x][y]
    
    # 분할정복 시작
    for i in range(x,x+r):
        for j in range(y,y+r):
            # 현재 기준과 다르면 4등분으로 분할
            if arr[i][j] != standard:
                r = r//2
                check(x,y,r,arr)
                check(x+r,y,r,arr)
                check(x,y+r,r,arr)
                check(x+r,y+r,r,arr)
                # 분할 후에는 리턴
                return
    # 분할되지 않았다면 현재 기준에 해당하는 값에 +1
    if standard == 1:
        cnt_1 += 1
    else:
        cnt_0 += 1

def solution(arr):
    global cnt_1, cnt_0
    n = len(arr)
    
    check(0,0,n,arr)
    
    return [cnt_0, cnt_1]
solution(	[[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]])