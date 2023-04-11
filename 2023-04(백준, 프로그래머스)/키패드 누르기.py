def solution(numbers, hand):
    nums = [[1,4,7],[2,5,8,0],[3,6,9]]
    hands = [[3,1]] + [[j,i] for j in range(3) for i in range(3)]
    l_h = [3,0]
    r_h = [3,2]
    
    result = ''
    for i in numbers:
        if i in nums[0]:
            result += 'L'
            l_h = hands[i]
        elif i in nums[2]:
            result += 'R'
            r_h = hands[i]
        else:
            l_r = abs(l_h[0] - hands[i][0]) + abs(l_h[1] - hands[i][1])
            r_r = abs(r_h[0] - hands[i][0]) + abs(r_h[1] - hands[i][1])
            if l_r == r_r:
                if hand == 'right':
                    result += 'R'
                    r_h = hands[i]
                else:
                    result += 'L'
                    l_h = hands[i]
            else:
                if l_r < r_r:
                    result += 'L'
                    l_h = hands[i]
                else:
                    result += 'R'
                    r_h = hands[i]
    return result

# 뭔가 더 간단한 방법이 있을거같으면서도 생각나지 않았다.
# 너무 노가다 식으로 코드를 작성한 느낌이랄까...