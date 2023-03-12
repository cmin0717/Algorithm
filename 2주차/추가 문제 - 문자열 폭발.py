import sys
input = sys.stdin.readline

word = input().rstrip()

explosion = input().rstrip()

check = [] 

for i in range(len(word)):
    check.append(word[i]) # 일단 글자는 바로 넣어준다.
    if ''.join(check[len(check)-len(explosion):]) == explosion: # 만약 글자를 넣는 와중에 폭발물 글자가 주어진다면
        for _ in range(len(explosion)): # 폭발물 글자 만큼 pop시켜준다.
            check.pop()

result = ''.join(check)
if not result:
    print('FRULA')
else:
    print(result)


# 시간 초과 (50퍼쯤?) - split, join를 이용해서 도전해보았다.
# while True:
#     a = len(word)
#     word = ''.join(word.split(explosion))
#     b = len(word)
#     if a == b:
#         print(word)
#         break
#     elif b == 0:
#         print('FRULA')
#         break
