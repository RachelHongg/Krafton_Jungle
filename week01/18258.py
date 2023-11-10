import sys
from collections import deque

T = int(sys.stdin.readline())

queue = deque()

for i in range(T):
    cyc = sys.stdin.readline().split()
    if cyc[0] == "push":
        queue.append(cyc[1])
    if cyc[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    if cyc[0] == "size":
        print(len(queue))
    if cyc[0] == "empty":
        if not queue:
            print(1)
        else: print(0)
    if cyc[0] == "front":
        if not queue:
            print(-1)
        else: print(queue[0])
    if cyc[0] == "back":
        if not queue:
            print(-1)
        else: print(queue[-1])

    
        