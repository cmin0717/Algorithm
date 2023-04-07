import sys
input = sys.stdin.readline

n,m = map(int,input().split())

n_set = list(map(int, input().split()))
m_set = list(map(int, input().split()))
all_set_cnt = (n + m) - len(set(n_set + m_set))

print((n - all_set_cnt) + (m - all_set_cnt))

# set(집합) -연산 메소드
# union - 합집합  - 예) a.union(b)
# intersection - 교집합  - 예) a.intersection(b)
# difference - 차집합  - 예) a.difference(b) -> a에서 b를 뺸 차집합
# symmetric_difference : 대칭차집합 연산자(합집합 - 교집합) -예) a.symmetric_difference(b) -> a,b의 각각의 차집합
# issubset : 부분집합이면 True, 아니면 False
# isdisjoint : 교집합이 없으면 True, 있으면 False