from itertools import *

pp_9 = [int(input()) for _ in range(9)]
pp_9.sort()

for i in range(9):
    for j in range(i+1,9):
        if sum(pp_9)-pp_9[i]-pp_9[j] == 100: # 2명의 사람을 뻇을 경우 값이 100이 된다면 그 두 난쟁이를 빼고 출력
            pp_9[i],pp_9[j] = 0,0 
            result = [i for i in pp_9 if i != 0]
            print(*result, sep='\n')
            exit() # 조합을 구했으니 종료

# combinations(iterable, r) : iterable에서 원소 개수가 r개인 조합 뽑기
# combinations_with_replacement(iterable,r) : iterable에서 원소 개수가 r개인 중복 조합 뽑기
# permutations(iterable,r) : iterable에서 원소 개수가 r개인 순열 뽑기
# product(*iterables, repeat=1) : 여러 iterable의 데카르트곱 리턴

# 라이브러리 사용해서 푼 코드
# li = list(combinations(pp_9, 7))

# for i in li:
#     if sum(i) == 100:
#         print(*sorted(i), sep='\n')
#         break

