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


ans = []
"""
while 1:
    N = int(input())
    if N == 0:break
    W = list(map(int, input().split()))
    ok = [[False] * (N+1) for _ in range(N+1)]

    for i in range(N+1):
        ok[i][i] = True

    for diff in range(2, N+1, 2):
        for l in range(N+1-diff):
            r = l+diff
            for mid in range(l+1, r):
                ok[l][r] |= ok[l][mid] & ok[mid][r]
            if l+1 <= r-1:
                ok[l][r] |= ok[l+1][r-1] & (abs(W[l]-W[r-1]) <= 1)
                
    dp = [0] * (N+1)
    for r in range(1, N+1):
        dp[r] = dp[r-1]
        for l in range(r):
            if ok[l][r]:
                dp[r] = max(dp[r], dp[l] + r-l)
    #ans.append(dp[N])
    print(dp[N])
#print(*ans)
"""

while 1:
    N = int(input())
    if N == 0:break
    W = list(map(int, input().split()))
    ok = [[-INF] * (N+1) for _ in range(N+1)]

    for i in range(N+1):
        ok[i][i] = 0

    for diff in range(1, N+1):
        for l in range(N+1-diff):
            r = l+diff
            if diff%2:
                ok[l][r] = max(ok[l+1][r], ok[l][r-1])
            else:
                for mid in range(l+1, r):
                    ok[l][r] = max(ok[l][r], ok[l][mid] + ok[mid][r])
                if l+1 <= r-1 and ok[l+1][r-1] == r-l-2 and abs(W[l]-W[r-1]) <= 1:
                    ok[l][r] = max(ok[l][r], ok[l+1][r-1] + 2)
    print(ok[0][N])
    ans.append(ok[0][N])
    #for row in ok:
        #print(row)
#print(*ans)