from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
squares = []
X = set()
Y = set()
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    squares.append((x1, y1, x2, y2))
    X.add(x1)
    X.add(x2)
    Y.add(y1)
    Y.add(y2)

X.add(0)
Y.add(0)
X = list(X)
Y = list(Y)

def CC(A: list) -> list:
    '座標圧縮'
    #index -> 実際の値のdict
    B = {}
    #実際の値 -> indexのdict
    C = {}
    for i, j in enumerate(sorted(A)):
        B[i] = j
        C[j] = i
    return B, C

CtoX, XtoC = CC(X)
CtoY, YtoC = CC(Y)

W = len(CtoX)
H = len(CtoY)
imos = [[0] * W for _ in range(H)]

for x1, y1, x2, y2 in squares:
    x1 = XtoC[x1]
    y1 = YtoC[y1]
    x2 = XtoC[x2]
    y2 = YtoC[y2]
    
    #座圧での二次元imos法では-1するindexに+1をしない(次の圧縮値との間をみるため)
    imos[y1][x1] += 1
    imos[y1][x2] -= 1
    imos[y2][x1] -= 1
    imos[y2][x2] += 1

for i in range(H):
    for j in range(1, W):
        imos[i][j] += imos[i][j-1]

for j in range(W):
    for i in range(1, H):
        imos[i][j] += imos[i-1][j]
    
ans = 0
for i in range(H-1):
    for j in range(W-1):
        if imos[i][j] >= 1:
            ans += (CtoY[i+1]-CtoY[i]) * (CtoX[j+1]-CtoX[j])
            
print(ans)
