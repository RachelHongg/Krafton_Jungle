def fact(n):
    if n == 0:
        return 1
    result = n * fact(n - 1)
    return result

n = int(input())   
print(fact(n))
   