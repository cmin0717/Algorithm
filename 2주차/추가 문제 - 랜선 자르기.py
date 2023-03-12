import sys
input = sys.stdin.readline

k,n = map(int,input().split())

lanline = [int(input()) for _ in range(k)]

start = 1
end = max(lanline) # 제일 긴 랜선
result = []

while start <= end:
    mid = (start + end) // 2
    cut_cnt = 0
    for i in lanline:
        cut_cnt += i // mid
    if cut_cnt >= n:
        result.append(mid) # n이상을 잘랐다면 일단 result에 저장
        start = mid+1 # 최대값을 얻기 위해 진행
    else:
        end = mid-1

print(max(result)) # n개 이상 만들수있는 길이중에 최대값 출력

