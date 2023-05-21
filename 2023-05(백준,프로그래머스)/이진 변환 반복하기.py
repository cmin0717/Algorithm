def solution(s):
    change, cut_zero = 0, 0
    
    def trans(word):
        trans_w = [w for w in word if w != '0']
        cz = len(word) - len(trans_w)
        new_w = bin(len(trans_w))[2:]
        return new_w,cz
    
    while s != '1':
        nw,cz = trans(s)
        s = nw
        cut_zero += cz
        change += 1
    
    return [change, cut_zero]