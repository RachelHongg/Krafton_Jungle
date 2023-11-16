import sys

N = int(sys.stdin.readline())

arr = [0]* (N + 1)

cnt = 0

def visited(x, y):
    for i in range(1, x + 1):
        if(arr[x] == arr[i]):   # 같은 줄
            return 1            # 실패
        if(abs(arr[x] - arr[i]) == abs(y - i)):     # 같은 대각선
            return 1            # 실패
        return 0            # 정상 종료

def n_queen(a):
    global cnt
    # base case
    if(a == N):
        cnt += 1
        return
    # 한 칸씩 넣으면서,
    for i in range(1, N):
        for j in range(1, N):
            if(visited(i, j) == 0):
                arr[i] = j
                n_queen(a + 1)
        
    # for j in range(1, N):
    #     arr[1] = j
    #     for i in range(2, N + 1):
    #         if(visited(i, j) == 0):
    #             arr[i] = j
    #             n_queen(a + 1)
    return cnt

a = n_queen(1)
print(cnt)
        
        
        

