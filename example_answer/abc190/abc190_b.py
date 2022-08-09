import sys
input = sys.stdin.readline

n, s, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]

for x, y in xy:
    if x < s and y > d:
        print("Yes")
        exit()

print("No")