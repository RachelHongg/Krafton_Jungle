import sys
from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1
    
    while pl <= pr:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
    return 0
    
n = int(sys.stdin.readline())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(sys.stdin.readline())
m_list = list(map(int, input().split()))


for i in range(len(m_list)):
    result= bin_search(n_list, m_list[i])
    print(result)

