from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

'''
その他の操作（最小値以外）
操作	segfunc	単位元
最小値	min(x, y)	float('inf')
最大値	max(x, y)	-float('inf')
区間和	x + y	0
区間積	x * y	1
最大公約数	math.gcd(x, y)	0
'''

#####segfunc#####
def segfunc(x, y):
    return max(x, y)

#################

#####ide_ele#####
ide_ele = -float('inf')
#################

class SegTree:
    '''
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    '''

    def __init__(self, init_val, segfunc, ide_ele):
        '''
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        '''
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        '''
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        '''
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        '''
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        '''
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
    
N = int(input())
frase = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[-INF] * 394 for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    l, r, p = frase[i-1]
    seg = SegTree([-INF] * 394, segfunc, ide_ele)
    for j in range(394):
        dp[i][j] = dp[i-1][j]
        left = max(j-r, 0)
        right = j-l
        if j-l >= 0:
            dp[i][j] = max(dp[i][j], seg.query(left, right+1) + p)
        seg.update(j, dp[i][j])

M = int(input())
ans = []
for _ in range(M):
    w = int(input())
    if dp[N][w] <= 0:
        print(-1)
        exit()
    else:
        ans.append(dp[N][w])

for i in ans:
    print(i)
    