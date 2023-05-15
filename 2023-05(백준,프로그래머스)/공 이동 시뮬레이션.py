def solution(n, m, x, y, queries):
    # 공이 이동할수있는 좌표 범위를 입력해준다. 처음에는 공의 현재 위치를 담는다.
    i,i1,j,j1 = x,x,y,y

    # 쿼리를 역순으로 돌리면서 공이 이동할수있는 범위를 구한다.
    for a,b in queries[::-1]:
        # 1번 타입 쿼리 : b만큼 y좌측 이동(우리는 우측으로 이동한다. 현재 역순으로 가고 있기에)
        if a == 0:
            # 최대범위 안에 들어오게 조정한다.
            j1 = min(j1+b,m-1)
            if j == 0: continue
            elif j+b < m:
                j = j+b
            else: return 0
        # 2번 타입 쿼리 : b만큼 y 우측 이동
        elif a == 1:
            j = max(0,j-b)
            if j1 == m-1: continue
            elif j1-b >= 0:
                j1 = j1-b
            else: return 0
        # 3번 타입 쿼리 : b만큼 x 위로 이동
        elif a == 2:
            i1 = min(i1+b, n-1)
            if i == 0: continue
            elif i+b < n:
                i = min(i+b, n-1)
            else: return 0
        # 4번 타입 쿼리 : b만큼 x 아래로 이동
        else:
            i = max(i-b, 0)
            if i1 == n-1: continue
            elif i1-b >= 0:
                i1 = max(i1-b,0)
            else: return 0
    
    # 최종 주어진 공의 범위를 계산해서 출력
    return (abs(i-i1) + 1) * (abs(j-j1) + 1)

# 처음 공의 위치에서 쿼리를 역순으로 돌린다.
# 쿼리를 돌리면서 공이 갈수있는 위치를 범위로 저장한다.
# 2번을 반복하면서 쿼리가 끝나면 현재 구한 범위를 통해 공이 갈수있는 위치를 반환
# 개빡세다 문제...디버깅 없이는 솔직히 못풀거같다.