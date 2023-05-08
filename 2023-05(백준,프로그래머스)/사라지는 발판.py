def solution(board, aloc, bloc):
    n,m = len(board),len(board[0]) # board의 가로세로 길이 저장

    def dfs(board,now,next,cnt):
        state = (cnt % 2 == 0) # 현재 누구 차례인지 파악 True면 A False면 B
        win,lose,x,y,check = [],[],now[0],now[1],False

        # 백트래킹
        board[x][y] = 0
        for r,c in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
            if 0 <= r < n and 0 <= c < m and board[r][c] != 0:
                check = True # 한곳이라도 갈수있다면 check를 True로 변환
                w, turn = dfs(board,next,[r,c],cnt+1)
                if w == state: # 현재 차례와 리턴받은 값이 같을경우만 win에 넣어준다.
                    win.append(turn)
                else:
                    lose.append(turn)
        board[x][y] = 1
        
        # 갈곳이 없다면 현재 차례사람이 진거니깐 다음 사람이 이긴거다.
        if not check:
            return (not state, cnt)
        
        # 현재 같은곳에 둘이 다있다면 다음 사람이 진것
        if now == next:
            return (state, cnt+1)
        
        # 만일 한번이라도 이겼다면 win에서 최단거리 한번도 이기지 못했다면 lose에서 최대거리
        return (state, min(win)) if win else (not state, max(lose))
            
    return dfs(board,aloc,bloc,0)[1]

solution(	[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2])


# def solution(board, aloc, bloc):
#     n,m = len(board),len(board[0])

#     def dfs(board,now,next,cnt):
#         x,y = now
#         state = (cnt % 2 == 0)
#         if now == next:
#             return (state, cnt+1)
        
#         min_d,max_d,check = float('inf'),0,False

#         board[x][y] = 0
#         for r,c in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
#             if 0 <= r < n and 0 <= c < m and board[r][c] != 0:
#                 check = True
#                 win,turn = dfs(board,next,[r,c],cnt+1)
#                 if win == state:
#                     min_d = min(min_d, turn)
#                 else:
#                     max_d = max(max_d, turn)
#         board[x][y] = 1

#         if check:
#             if min_d != float('inf'):
#                 return (state,min_d)
#             else:
#                 return (state,max_d)
#         else:
#             return (state, cnt)
    
#     return dfs(board,aloc,bloc,0)[1]




# def solution(board, aloc, bloc):
#     n,m = len(board), len(board[0])

#     def dfs(a,b,a1,b1,cnt):
#         check,win,lose = False,[],[]
#         x,y,x1,y1 = a1,b1,a,b

#         if board[x][y] == 0:
#             return (cnt % 2 != 0, cnt)

#         board[x][y] = 0
#         for r,c in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
#             if 0 <= r < n and 0 <= c < m and board[r][c] != 0:
#                 check = True 
#                 w,turn = dfs(r,c,x1,y1,cnt+1)
#                 if w:
#                     win.append(turn)
#                 else:
#                     lose.append(turn)
#         board[x][y] = 1

#         if check:
#             if win:
#                 return (True,min(win)) if cnt%2 == 0 else (False,min(win))
#             else:
#                 return (False,max(lose)) if cnt%2 == 0 else (True,max(lose))
#         else:
#             return (cnt % 2 != 0,cnt)
    
#     return dfs(bloc[0],bloc[1],aloc[0],aloc[1],0)[1]