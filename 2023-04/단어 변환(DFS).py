def solution(begin, target, words):
    
    def check(b,li): # dfs를 통해 target를 만들수있는지 확인
        if b == target:
            result.append(len(li)) # 변환과정의 길이를 담고 리턴
            return
        
        for word in words:
            if word != b and word in li:
                continue
            cnt = 0
            for i in range(len(word)):
                if b[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                check(word, li + [b]) # 시작값을 바꾼 값으로, 방문 체크
                
    result = []
    check(begin,[])
    
    if len(result) == 0:
        return 0
    else:
        return min(result)


# 파이썬 yield를 사용한 풀이 (신기해서 가져옴 알고있으면 유용할듯하다.)
# from collections import deque

# def get_adjacent(current, words):
#     for word in words:
#         if len(current) != len(word):
#             continue

#         count = 0
#         for c, w in zip(current, word):
#             if c != w:
#                 count += 1

#         if count == 1:
#             yield word # yield호출시 함수안에서의 작업은 잠시 중단하고 함수 caller에게 제어권이 넘어간다. caller가 리턴값 처리후 다시 제어권을 넘김


# def solution(begin, target, words):
#     dist = {begin: 0}
#     queue = deque([begin])

#     while queue:
#         current = queue.popleft()

#         for next_word in get_adjacent(current, words): # yield 리턴값이 생길시 실행된다. 실행후 다시 yield가 실행된 함수로 제어권이 넘어감
#             if next_word not in dist:
#                 dist[next_word] = dist[current] + 1
#                 queue.append(next_word)

#     return dist.get(target, 0)
solution('hit','cog',["hot", "dot", "dog", "lot", "log", "cog"])