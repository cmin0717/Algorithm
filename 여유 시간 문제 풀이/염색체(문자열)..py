import sys
input = sys.stdin.readline

tree_dic = {}

while True:
    tree = input().rstrip()
    # 몇개의 입력이 오는지 모르는 문제는 마지막 입력이 ''이면 종료인듯하다.
    if tree == '':
        break
    if tree_dic.get(tree) == None:
        tree_dic[tree] = 1
    else:
        tree_dic[tree] += 1

total = sum(tree_dic.values())
result = sorted(tree_dic.keys())
for tree in result:
    n = (tree_dic[tree] / total) * 100
    print("{} {:.4f}".format(tree, n)) # 소숫점 포맷팅을 기억하자