import math
import sys

n = 10000

def prime():
    list = [True] * n
    m = int(math.sqrt(n))
    for i in range(2, m + 1):
        if list[i] == True:
            for j in range(i+i, n, i):
                list[j] = False
    return [i for i in range(2, n) if list[i] == True]

x = int(sys.stdin.readline())

if x % 2 == 0:
    x_1 = x // 2
    x_2 = x // 2


primes = prime()
   
for i in range(len(prime())):
    if primes[i] == x_1:
        for j in range(len(prime())):
            if primes[j] == x_2:
                print(x_1, x_2)
    else:
        x_1 -= 1
        x_2 += 1

    
    
    
        