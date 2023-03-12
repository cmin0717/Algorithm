n = int(input())

tree = {}
for _ in range(n):
    node = list(input().split())
    tree[node[0]] = [node[1], node[2]] # 입력 받은 노드를 딕셔너리에 루트는 키로 벨류는 [왼.자, 오.자]로 넣어서 저장

pre,ino,pos = '','','' 

def pre_t(x): # 전위 순회(루트 -> 왼.자 -> 오.자)
    global pre
    if x != '.': # 전위 순회 순서대로 진행, 입력받은 루트가 나올 타이밍에 pre에 추가
        pre += x 
        pre_t(tree[x][0])
        pre_t(tree[x][1])

def ino_t(x): # 중위 순회 (왼.자 -> 루트 -> 오.자)
    global ino
    if x != '.': # 위와 동일
        ino_t(tree[x][0])
        ino += x
        ino_t(tree[x][1])

def pos_t(x): # 후위 순회 (왼.자 -> 오.자 -> 루트)
    global pos
    if x != '.':
        pos_t(tree[x][0])
        pos_t(tree[x][1])
        pos += x

pre_t('A') # 루트는 'A'로 무조건 실행한다고 하니 A를 넣어 실행
ino_t('A')
pos_t('A')
print(pre, ino, pos, sep='\n') # 순회를 다 돌고 난 값들 출력