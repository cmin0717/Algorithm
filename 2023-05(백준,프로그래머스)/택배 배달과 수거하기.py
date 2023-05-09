# def solution(cap, n, deliveries, pickups):
    
#     d,p = {},{}
    
#     for i in range(1,n+1):
#         d.setdefault(i,0)
#         p.setdefault(i,0)
    
#     sd,sp = 0,0
#     for i in range(n-1,-1,-1):
#         if deliveries[i]:
#             sd += deliveries[i]
#             turn = sd//cap if sd % cap == 0 else (sd//cap) +1
#             if d[turn] == 0:
#                 d[turn] = i
#         if pickups[i]:
#             sp += pickups[i]
#             turn = sp//cap if sp % cap == 0 else (sp//cap) +1
#             if p[turn] == 0:
#                 p[turn] = i
#     print(d,p)
        

# solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])

dic = {}
print(list(dic.items()))