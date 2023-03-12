import sys
input = sys.stdin.readline

m = int(input())

quad_trees = [input().rstrip() for _ in range(m)] 

def tree(x,n,zips):
    if len(x) == 1:
        return x[0]
    quad_tree = x
    quad_1 = [quad_tree[i][:n//2] for i in range(n//2)] # 각 분사면에 있는 숫자를 모아준다.
    quad_2 = [quad_tree[i][n//2:] for i in range(n//2)]
    quad_3 = [quad_tree[i][:n//2] for i in range(n//2,n)]
    quad_4 = [quad_tree[i][n//2:] for i in range(n//2,n)]

    for i in quad_1,quad_2,quad_3,quad_4: # 4개의 분사면을 돌면서 글자압축
        if len(set(i)) == 1:
            check = [j for j in i[0]]
            if len(set(check)) == 1:
                zips += check[0][0] # 다 같은 숫자로 이루어져있다면 그 숫자 추가
            else:
                zips += tree(i, n//2,'') # 그렇지 않다면 다시 tree함수에 넣어 나온 숫자를 추가
        else:
            zips += tree(i,n//2,'') # 위와 같다
    zips = '(' + zips + ')' # 각 재귀가 끝나고 마지막에 추가한 글자를 ()로 감싸서 return해준다.
    return zips
result = tree(quad_trees,m,'')

check = []
for i in result:
    if i != '(' and i != ')':
        check.append(i)
if len(set(check)) == 1: # 모든 분사면이 다 같은 숫자로 이루어졌다면
    print(check[0]) # 이루어진 숫자 출력
else:
    print(result)

# 다른 사람 풀이 (이게 쫌더 재귀에 어울리는 풀이법 같다....)
# def quadtree(y, x, n):
#     standard = l[y][x] # 처음 기준 숫자를 정하고

#     for i in range(y, y+n):
#         for j in range(x, x+n):
#             if l[i][j] != standard: # 기준 숫자와 달라지면 4등분해서 다시 재귀
#                 print('(', end='') # 재귀 시작과 끝에 ()를 추가 해준다.
#                 quadtree(y, x, n//2) # 좌표값에 i,j를 넣어주는게 아니라 원래 받은 x,y를 넣어주어야한다
#                 quadtree(y, x+n//2, n//2)
#                 quadtree(y+n//2, x, n//2)
#                 quadtree(y+n//2, x+n//2, n//2)
#                 print(')', end='')
#                 return

#     if standard == 0: # 아무것도 안걸리고 왔다면 0 혹은 1을 출력
#         print('0', end='')
#     else:
#         print('1', end='')


# n = int(input())
# l = []
# for i in range(n):
#     l.append(list(map(int, input().rstrip())))

# quadtree(0, 0, n)