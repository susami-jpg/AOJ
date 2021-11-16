from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

setrecursionlimit(10**7)

while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    maze = [list(map(int, input().split())) for _ in range(h)]
    
    def valid(y, x):
        return 0 <= x < w and 0 <= y < h and maze[y][x]
    
    def dfs(y, x):
        if seen[y][x]:
            return
        seen[y][x] = 1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:continue
                nexty = y + i
                nextx = x + j
                if valid(nexty, nextx) and seen[nexty][nextx] == 0:
                    dfs(nexty, nextx)
        return
    
    ans = 0
    seen = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if seen[i][j] == 0 and maze[i][j]:
                ans += 1
                dfs(i, j)
    print(ans)
    