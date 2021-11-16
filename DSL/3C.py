from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

def syakutori(A, K):
    #配列Aの連続部分列の和がK以下となるような(i, j)の組の個数を数える
    A = [0] + A
    n = len(A)
    r = 0
    S = 0
    ans = 0
    for l in range(n-1):
        while r+1 < n and S + A[r+1] <= K:
            S += A[r+1]
            r += 1
        ans += r-l
        S -= A[l+1]
    return ans

def syakutori2(A, K):
    #配列Aの連続部分列の和がKより大きくなるような(i, j)の組の個数を数える
    A = [0] + A
    n = len(A)
    r = 0
    S = 0
    ans = 0
    for l in range(n-1):
        while r+1 < n and S + A[r+1] <= K:
            S += A[r+1]
            r += 1
        #nは1indexにするための調整である[0]を含んだ数(もとの配列の長さ+1)になっているので-1する
        ans += n-1-r
        S -= A[l+1]
    return ans

print(N*(N+1)//2)
for x in X:
    print(syakutori(A, x))
    print(syakutori2(A, x))
    