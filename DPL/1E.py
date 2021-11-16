from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

def rsd(s1, s2):
    x = len(s1)
    y = len(s2)
    s1 = " " + s1
    s2 = " " + s2
    dp = [[0] * (x+1) for _ in range(y+1)]
    for j in range(x+1):
        dp[0][j] = j
    for i in range(y+1):
        dp[i][0] = i
    for i in range(1, y+1):
        for j in range(1, x+1):
            if s1[j] == s2[i]:
                diff = 0
            else:
                diff = 1
            dp[i][j] = min(dp[i-1][j-1] + diff, dp[i-1][j] + 1, dp[i][j-1] + 1)
    return dp[y][x]

s1 = input()
s2 = input()
print(rsd(s1, s2))

