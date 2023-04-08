def solution(n, m, x, y, r, c, k):
    maze = [['.']*(m+1) for _ in range(n+1)]
    maze[x][y] = 's'
    maze[r][c] = 'e'
    
    # 갈수 있는지 없는지 판단
    h = (abs(x-r) + abs(y-c))
    if h % 2 != k % 2 or h > k:
        return 'impossible'
    
    check = ''
    # 거리가 남는다면 d,l를 계속 쓰는것이 사전순으로 빠르다.
    while (abs(x-r) + abs(y-c)) != k-len(check): # 현재 위치에서 도착지까지 거리가 딱 맞을때 까지 반복
        if 1 <= x+1 <=n and 1 <= y <= m:
            check += 'd'
            x += 1
            continue
        if 1 <= x <=n and 1 <= y-1 <= m:
            check += 'l'
            y -= 1
            continue
        # 좌측 하단으로 왔다면 l,r반복
        check += 'r'
        y += 1
    
    # 만일 처음부터 거리가 딱 맞다면
    if x-r < 0:
        check += 'd' * abs(x-r)
    if c-y < 0:
        check += 'l' * abs(c-y)
    # 아니라면 좌측하단에서 목표까지 가야하니깐 더해준다.
    check += 'r' * (c-y)
    check += 'u' * (x-r)
    return check


# 시간 초과 1
# result = 'z'*2501
# def solution(n, m, x, y, r, c, k):
#     global result
#     maze = [['.']*(m+1) for _ in range(n+1)]
#     maze[x][y] = 's'
#     maze[r][c] = 'e'
    
#     def check(a,b,cnt,word):
#         global result
#         if a == r and b == c and cnt == k:
#             result = sorted([result,word])[0]
#             return
        
#         if cnt == k:
#             return
        
#         if sorted([result,word])[0] == result:
#             return

#         for i,j,w in [a+1,b,'d'],[a-1,b,'u'],[a,b+1,'r'],[a,b-1,'l']:
#             if 1 <= i <= n and 1 <= j <= m:
#                 check(i,j,cnt+1,word+w)
    
#     check(x,y,0,'')
    
#     if len(result) == 2501:
#         return "impossible"
#     else:
#         return result

# 시간 초과 2
# def solution(n, m, x, y, r, c, k):
#     maze = [['.']*(m+1) for _ in range(n+1)]
#     maze[x][y] = 's'
#     maze[r][c] = 'e'
    
#     check = ''
#     while (abs(x-r) + abs(y-c)) != k-len(check):
#         if 1 <= x+1 <=n and 1 <= y <= m:
#             check += 'd'
#             x += 1
#             continue
#         if 1 <= x <=n and 1 <= y-1 <= m:
#             check += 'l'
#             y -= 1
#             continue
#         check += 'r'
#         y += 1
    
#     result = [[x,y,len(check),check]]
    
#     while result:
#         a,b,cnt,word = result.pop()
        
#         if a == r and b == c and cnt == k:
#             return word

#         if cnt == k:
#             continue

#         for i,j,w in [a-1,b,'u'],[a,b+1,'r'],[a,b-1,'l'],[a+1,b,'d']:
#             if 1 <= i <= n and 1 <= j <= m:
#                 result.append([i,j,cnt+1,word+w])
#     else:
#          return 'impossible'

solution(3,4,2,3,3,1,5)