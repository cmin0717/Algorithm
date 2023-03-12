import sys
input = sys.stdin.readline

star = ["***", "* *", "***"]

n = int(input())

def make_star(n):
    if n == 3:
        return star
    new_star = []
    for i in make_star(n//3):
        new_star.append(i*3)
    for j in make_star(n//3):
        new_star.append(j + ' '*int(n//3) + j)
    for l in make_star(n//3):
        new_star.append(l*3)
    return new_star

for x in make_star(n):
    print(x)