def solution(a):
    # 해당 수열에서 각 숫자들의 인덱스와 해당 숫자가 총 몇개있는지 구한다.
    cnt = {}
    for i in range(len(a)):
        cnt.setdefault(a[i], [a[i],0,[]])
        cnt[a[i]][1] += 1
        cnt[a[i]][2].append(i)
    
    # 가장 많은 숫자별로 정렬
    ls = sorted(cnt.values(), key=lambda x: -x[1])
    
    # 각 숫자로 이루어진 부분수열 개수구하기
    def check(n, arr):
        count,start = 0, 0
        arr = arr + [len(a)]

        for i in range(len(arr)-1):
            # 부분 수열이 될수있는지 판단
            temp = True
            # 해당 인덱스에서 왼쪽 탐색
            if start < arr[i]:
                for j in range(start, arr[i]):
                    if a[j] != n:
                        start = arr[i]+1
                        temp = False
                        break
            # 왼쪽에서 찾지 못했다면 오른쪽 탐색
            if temp:
                for j in range(arr[i]+1, arr[i+1]):
                    if a[j] != n:
                        start = j+1
                        temp = False
                        break
            # 둘다 찾지못했다면 시작점을 다음 인덱스로 넘김 찾았다면 +1
            if temp:
                start = arr[i+1]+1
            else:
                count += 1
        return count
    
    result = 0
    for n, c, arr in ls:
        if c <= result:
            break
        result = max(result, check(n, arr))
    
    return result*2