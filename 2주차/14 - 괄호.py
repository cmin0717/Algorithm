n = int(input())

bracket = [input() for _ in range(n)]

for i in bracket:
    li_cket = [j for j in i]
    cnt = 0
    while len(li_cket) != 0:
        if li_cket.pop() == ')': # ')'이 나왔다면 cnt에 1을 더해준다.
            cnt += 1
        else:
            if cnt == 0: # cnt = 0이라는 말은 ')'이게 한개도 없다는 말인데 거기에서 '('이게 나왔다면 바로 끝!
                print('NO')
                break
            else: # cnt != 0아니고 '('이게 나오면 cnt -= 1를 해준다.
                cnt -= 1
    else:
        if cnt == 0: # 최종으로 다 확인하고 cnt = 0이라면 '(',')' 요게 짝으로 잘맞게 나온거니깐 YES
            print('YES')
        else:
            print('NO')


# replace를 이용한 풀이 스텍이 아니기에 패쓰!
# for i in bracket:
#     for _ in range(26):
#         i = i.replace('()','')
#         if len(i) == 0:
#             print('YES')
#             break
#     else:
#         print('NO')