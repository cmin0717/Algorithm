import sys
input = sys.stdin.readline

n,m = map(int,input().split())

cd = list(map(int,input().split()))

start = max(cd) # 강의를 cd에 넣으려면 강의의 최대크기를 무조건 넣어야하기에 최소는 cd의 최대크기로 시작
end = sum(cd) # 모든 강의를 한곳에 다넣을수도 있기에 end는 cd의 총합으로함
result = 10000 * 100000 + 1

while start <= end:
    mid = (start + end) // 2
    sum_cd = 0
    cd_cnt = 0
    for i in range(n):
        if sum_cd + cd[i] > mid: # mid범위를 넘어가면 새로운 cd에 담아야하므로 cnt +1해주고 다시 합은 0으로 변경
            cd_cnt += 1
            sum_cd = 0
        sum_cd += cd[i] 
    if sum_cd: # for문이 끝나고도 sum_cd에 값이 있다면 마지막 cd에 담긴거니깐 cnt += 1 해준다.
        cd_cnt += 1
    if cd_cnt > m: # 만일 cnt가 m보다 크다면 cd크기를 늘린다.
        start = mid +1
    else:
        result = min(result,mid) # cd_cnt가 m보다 작다면 m개만큼도 만들수있다 넉넉히, 최소값을 구해야하니깐 min함수로 최소값 저장
        end = mid -1 # 현재 최소값보다 더 작은값이 있을수있으니 진행

print(result)