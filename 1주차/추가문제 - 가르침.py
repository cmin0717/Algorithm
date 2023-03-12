# 백트래킹
n,k = map(int,input().split())
words = [set(input()[4:-4]) for _ in range(n)] # 'anta','tica'는 가져올 필요가 없기에 거기 사이에 있는 문자만 가져온다.
alpha = [False] * 26 # 배운 문자를 기록하기 위해 알파벳 개수만큼 만들어준다.
max_words = 0

if k < 5: # k가 5보다 작다면 연산할 필요없이 바로 출력
    print(0)
    exit()

for i in ['a','n','t','i','c']: # 필수로 배워야하는 문자이기에 미리 배운 문자에 넣어준다.
    alpha[ord(i) -97] = True 

def dsf(i,learn):
    global max_words

    if learn == k-5:
        cnt = 0
        for x in words: # 배울수있는 문자를 다 배웠다면 이제 처음 주어진 단어를 읽을수 있는지 확인
            for y in x:
                if not alpha[ord(y)-97]:
                    break
            else:
                cnt += 1
        max_words = max(cnt, max_words) # 최신 최대값을 계속 유지
        return  max_words

    for j in range(i,26): # 알파벳을 순서대로 모든 경우의 수를 탐색
        if not alpha[j]:
            alpha[j] = True
            dsf(j,learn+1)
            alpha[j] = False

dsf(0,0)
print(max_words)


# 비트 마스킹
# n, k = map(int, input().split())
# if k < 5:
#     print(0)
# else:
#     k -= 5
#     nece_chars = {'a', 'n', 't', 'i', 'c'}
#     input_chars = []
#     alpha = {ky: v for v, ky in enumerate(
#         (set(map(chr, range(ord('a'), ord('z')+1))) - nece_chars))}
#     cnt = 0
#     for _ in range(n):
#         tmp = 0
#         for c in set(input())-nece_chars:
#             tmp = tmp | (1 << alpha[c])
#         input_chars.append(tmp)
#     power_by_2 = (2**i for i in range(21))
#     for comb in combinations(power_by_2, k):
#         test = sum(comb)

#         ct = 0
#         for cb in input_chars:
#             if test & cb == cb:
#                 ct += 1

#         cnt = max(cnt, ct)
#     print(cnt)