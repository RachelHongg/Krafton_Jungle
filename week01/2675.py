T = int(input())

for i in range(T):
    a, b = input().split()
    a = int(a)
    b = str(b)
    for j in range(len(b)):
        print(a * b[j], end="") # 옆으로 넘김
    print('') # 줄 넘김
    