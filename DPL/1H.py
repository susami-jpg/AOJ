from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, W = map(int, input().split())
bag = [tuple(map(int, input().split())) for _ in range(N)]
S1 = N//2
S2 = N-S1
bag1 = bag[:S1]
bag2 = bag[S1:]

def harf_all_search(S, bag):
    rec = defaultdict(int)
    for i in range(1<<S):
        w = 0
        v = 0
        for j in range(S):
            if (i>>j)&1:
                v += bag[j][0]
                w += bag[j][1]
        if w <= W:
            rec[w] = max(rec[w], v)
    return rec

rec1 = dict(harf_all_search(S1, bag1))

rec = dict(harf_all_search(S2, bag2))
max_val = 0
key_set = []
rec2 = defaultdict(int)
for key, val in sorted(rec.items()):
    key_set.append(key)
    rec2[key] = max_val = max(max_val, val)
    
def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

ans = 0
max_val = -1
for key, val in sorted(rec1.items()):
    max_val = max(max_val, val)
    if val < max_val:continue
    rest = W-key
    _, ind = OrLessThan(rest, key_set)
    ind = key_set[ind]
    ans = max(ans, rec2[ind]+val)
print(ans)
