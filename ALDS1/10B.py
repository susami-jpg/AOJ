from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**15
MOD = 10**9+7

N = int(input())
M = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[INF] * (N+1) for _ in range(N+1)]
for i in range(N):
    dp[i][i+1] = 0

for diff in range(2, N+1):
    for l in range(N+1-diff):
        r = l + diff
        for k in range(l, r):
            #print(l, k, dp[l][k])
            #print(k, r, dp[k][r])
            r1 = M[l][0]
            c2 = M[r-1][1]
            c1 = M[k][0]
            dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r] + r1 * c2 * c1)
    
print(dp[0][N])

            