import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    char = list(input().rstrip().split())
    tree[char[0]] = [char[1],char[2]] # 딕셔너리 형태로 노드값의 왼.자, 오.자를 벨류값으로 저장

pre,ino,pos = '','',''

def pre_tr(x): # 노드 -> 왼.자 -> 오.자 이므로 노드값을 pre에 추가 -> 왼.자 재귀 -> 오.자 재귀
    global pre
    if x != '.': # 빈칸이 아닐경우
        pre += x 
        pre_tr(tree[x][0])
        pre_tr(tree[x][1])

def ino_tr(x): # 왼.자 -> 노드 -> 오.자 이므로 왼.자 재귀 -> 노드 값 ino에 추가 -> 오.자 재귀
    global ino
    if x != '.':
        ino_tr(tree[x][0])
        ino += x
        ino_tr(tree[x][1])

def pos_tr(x): # 왼.자 -> 오.자 -> 노드 이므로 왼.자 재귀 -> 오,자 재귀 -> 노드값 pos에 추가
    global pos
    if x != '.':
        pos_tr(tree[x][0])
        pos_tr(tree[x][1])
        pos += x

pre_tr('A')
ino_tr('A')
pos_tr('A')
print(pre,ino,pos,sep='\n')


# pre = ''
# def pre_tr(x):
#     global pre
#     pre += x
#     if tree[x][0] != '.':
#         pre_tr(tree[x][0])
#     if tree[x][1] != '.':
#         pre_tr(tree[x][1])
# pre_tr('A')

# ino = ''
# def ino_tr(x):
#     global ino
#     if tree[x][0] == '.':
#         ino += x
#     if tree[x][0] != '.':
#         ino_tr(tree[x][0])
#         if x not in ino: ino += x
#     if tree[x][1] != '.':
#         ino_tr(tree[x][1])
#         if x not in ino: ino += x
# ino_tr('A')

# pos = ''
# def pos_tr(x):
#     global pos
#     if tree[x][0] == '.' and tree[x][1] == '.':
#         pos += x
#         return
#     if tree[x][0] != '.':
#         pos_tr(tree[x][0])
#         if tree[x][1] != '.':
#             pos_tr(tree[x][1])
#             pos += x
#         else:
#             pos += x
#     else:
#         pos_tr(tree[x][1])
#         pos += x
# pos_tr('A')
# print(pre,ino,pos,sep='\n')