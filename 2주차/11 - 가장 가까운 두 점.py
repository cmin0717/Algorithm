import sys
N = int(sys.stdin.readline())
point = []
for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    point.append((x, y))
point.sort()

def getDist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solution(left, right):
    if left == right:
        return float('inf')
    else:
        mid = (left + right) // 2
        min_dist = min(solution(left, mid), solution(mid + 1, right))
        target_list = []
        
        for i in range(mid, left - 1, -1):
            if (point[i][0] - point[mid][0]) ** 2 < min_dist:
                target_list.append(point[i])
            else:
                break

        for j in range(mid + 1, right + 1):
            if (point[j][0] - point[mid][0]) ** 2 < min_dist:
                target_list.append(point[j])
            else:
                break
                
        target_list.sort(key=lambda x: x[1])
        for i in range(len(target_list) - 1):
            for j in range(i + 1, len(target_list)):
                if (target_list[i][1] - target_list[j][1]) ** 2 < min_dist:
                    dist = getDist(target_list[i], target_list[j])
                    min_dist = min(min_dist, dist)
                else:
                    break
        return min_dist

if len(point) != len(set(point)):
    print(0)
else:
    print((solution(0, len(point) - 1)))

# 답을 봐도 잘모르겠다.....