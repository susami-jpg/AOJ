from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, W = map(int, input().split())
bag = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W+1) for _ in range(N+1)]
for i in range(1, N+1):
    v, w = bag[i-1]
    for j in range(W+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])
        if j-w >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j-w] + v)
#for row in dp:
    #print(row)
print(dp[N][W])

