from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

while 1:
    N, M = map(int, input().split())
    if N==M==0:
        break
    A = list(map(int, input().split()))
    a = A[0]
    A = A[1:]
    B = list(map(int, input().split()))
    b = B[0]
    B = B[1:]
    C = list(map(int, input().split()))
    c = C[0]
    C = C[1:]

    goal = [i for i in range(1, N+1)]
    deq = deque()
    deq.append((A, B, C, 0, -1))
    ans = INF
    while deq:
        x, y, z, d, prev = deq.popleft()
        if x == goal or z == goal:
            ans = d
            break
        if x:
            A_last = x[-1]
        else:
            A_last = 0
        if y:
            B_last = y[-1]
        else:
            B_last = 0
        if z:
            C_last = z[-1]
        else:
            C_last = 0
        
        if A_last > B_last:
            nextx = x[:-1]
            nexty = y + [A_last]
            if prev != (nextx, nexty, z):
                deq.append((nextx, nexty, z, d+1, (x, y, z)))
        elif A_last < B_last:
            nextx = x + [B_last]
            nexty = y[:-1]
            if prev != (nextx, nexty, z):
                deq.append((nextx, nexty, z, d+1, (x, y, z)))
        if C_last > B_last:
            nextz = z[:-1]
            nexty = y + [C_last]
            if prev != (x, nexty, nextz):
                deq.append((x, nexty, nextz, d+1, (x, y, z)))
        elif C_last < B_last:
            nextz = z + [B_last]
            nexty = y[:-1]
            if prev != (x, nexty, nextz):
                deq.append((x, nexty, nextz, d+1, (x, y, z)))

    if ans > M:
        print(-1)
    else:
        print(ans)
        