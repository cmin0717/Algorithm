def solution(n):
    num = ''
    
    while n != 0:
        d,m = divmod(n,3)
        num += str(m)
        n = d
    
    return int(num, 3)