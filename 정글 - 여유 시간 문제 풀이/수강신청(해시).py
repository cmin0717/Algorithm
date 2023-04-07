import sys
input = sys.stdin.readline

k, l = map(int,input().split())
store = {} # 각 키값에 해당하는 순위를 저장할 딕셔너리

for turn in range(l):
    store[input().rstrip()] = turn

result = sorted(list(store.items()) ,key=lambda x:x[1]) # item함수를 통해 키값과 벨류값을 가져오고 순위순으로 정렬시킨다.
for key,value in result[:k]:
    print(key)

