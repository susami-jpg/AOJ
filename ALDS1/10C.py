from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

def lcs(X, Y):
    x = len(X)
    y = len(Y)
    X = " " + X
    Y = " " + Y
    dp = [[0] * (x+1) for _ in range(y+1)]
    for i in range(1, y+1):
        for j in range(1, x+1):
            if X[j] == Y[i]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[y][x]

q = int(input())
for _ in range(q):
    X = input()
    Y = input()
    print(lcs(X, Y))

