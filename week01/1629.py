import sys

num, cyc, div = map(int,sys.stdin.readline().split())
res = num

def multi(cyc):
    global res
    # base case
    if(cyc == 1):
        return res % div
    else:
        res = multi(cyc // 2)
        if(cyc % 2 == 0):
            return (res * res) % div
        else:
            return (num * (res * res)) % div
            
a = multi(cyc)
print(a)