def solution(sizes):
    max_len = 0
    min_max_len = 0
    for x,y in sizes:
        max_len = max(max_len, x, y)
        min_max_len = max(min_max_len, min(x,y))
    return max_len * min_max_len
