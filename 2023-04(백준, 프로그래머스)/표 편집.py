class node:
    def __init__(self,left = None,right = None):
        self.remove = False
        self.left = left
        self.right = right
def solution(n, k, cmds):
    link = [node(i-1,i+1) for i in range(n)]
    link[0].left = None
    link[-1].right = None
    now = k
    check = []

    for cmd in cmds:
        if cmd[0] == 'U':
            c,num = cmd.split()
            for _ in range(int(num)):
                now = link[now].left
        elif cmd[0] == 'D':
            c,num = cmd.split()
            for _ in range(int(num)):
                now = link[now].right
        elif cmd[0] == 'C':
            check.append(now)
            link[now].remove = True
            l,r = link[now].left, link[now].right

            if l != None:
                link[l].right = r
            if r:
                link[r].left = l
                now = r
            else:
                now = l
        else:
            p = check.pop()
            link[p].remove = False
            l,r = link[p].left, link[p].right
            if l:
                link[l].right = p
            if r:
                link[r].left = p
                
    result = ['X' if i.remove else 'O' for i in link]
    return ''.join(result)