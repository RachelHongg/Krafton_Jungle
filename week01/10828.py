import sys

n = int(sys.stdin.readline())

stk = []

for i in range(n):
    cyc = sys.stdin.readline().split()
    if cyc[0] == 'push':
        stk.append(cyc[1])
    elif cyc[0] == 'pop':
        if len(stk) > 0:
            print(stk.pop())
        else:
            print(-1)
    elif cyc[0] == 'size':
        print(len(stk))
    elif cyc[0] == 'empty':
        if len(stk) == 0:
            print(1)
        else: 
            print(0)
    elif cyc[0] == 'top':
        if len(stk) > 0: print(stk[-1])
        else: print(-1)
        
        