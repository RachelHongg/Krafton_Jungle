import sys
from heapq import heappop, heappush

T = int(sys.stdin.readline())
heap = []

for i in range(T):
    n = int(sys.stdin.readline())
    if n == 0:
        if not heap:
            print(0)
        else:
            # _, max = heappop(heap)
            # print(max)
            print(heappop(heap)[1])
    else:
        heappush(heap, (-n, n))