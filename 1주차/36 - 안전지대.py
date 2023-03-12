import sys, copy
input = sys.stdin.readline

n = int(input())
areas = []
check_area = []
max_high = 0

for i in range(n):
    area = list(map(int,input().split()))
    max_high = max(max_high,max(area)) # 도시에서 가장 높은 지대를 미리 구한다.
    areas.append(area) # 지대별로 구성된 지도를 만듬
    check_area += area # 도시에 존재하는 지대만 탐색하기 위해 지대만 모아놓은 리스트 생성


def serch_area(arr,h): # copy본 지도와 비가 내린 양
    save_area = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h:
                arr[i][j] = 0 # 지도를 돌면서 물에 잠기지 않은 지역을 0으로 변경 그래야 다음 탐색에서 중복으로 걸리지 않는다.
                save_area += 1
                check = [[i,j]] # 물에 잠기지 않은 지역을 좌표로 저장
                while check:
                    # nonlocal i 같은 변수명을 사용하려면 nonlocal을 사용해주어야 한다.
                    # nonlocal j
                    row,col = check.pop() # 좌표에서 하나씩 꺼내온다.
                    for x,y in [row+1,col], [row,col+1], [row-1,col], [row,col-1]: # 해당칸의 상하좌우 좌표를 확인한다.
                        if 0 <= x < n and 0 <= y < n and arr[x][y] > h: # 조건을 만족하면 이전 칸이랑 붙어있는거니깐 0을 입력하고 다시 반복
                            arr[x][y] = 0
                            check.append([x,y])
    return save_area

max_save_area = 1
for i in set(check_area): # set함수를 이용하여 중복 지대를 지우고 탐색  # max_high를 이용하여 0 ~ max_high까지 돌려도 해결할수있다.
    cp_areas = copy.deepcopy(areas) # 지도를 변경해야함으로 copy본을 사용
    max_save_area = max(max_save_area, serch_area(cp_areas, i))

print(max_save_area)




# 짜다 실패한 코드
# def save_cnt(i,j,cnt,test_area):
#     if not test_area[i][j] :
#         test_area[i][j] = cnt
#         save_cnt(i+1,j,cnt,test_area)
#         save_cnt(i,j+1,cnt,test_area)
#         save_cnt(i-1,j,cnt,test_area)
#         save_cnt(i,j-1,cnt,test_area)
#     else:
#         return

# for m in range(101):
#     check_area = [[True] * (n+2)] + [[True] + [False] * (n) + [True]] * n + [[True] * (n+2)]
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if area[i-1][j-1] < m:
#                 check_area[i][j] = True  -> 여기서 값이 부분만 변하는게 아니라 다변한다....이유를 찾지 못함
#     cnt = 0
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if not check_area[i][j]:
#                 cnt += 1
#                 save_cnt(i,j,cnt,check_area)
#     if cnt == 0:
#         break
#     else:
#         max_save_area = max(max_save_area, cnt)

# print(max_save_area)