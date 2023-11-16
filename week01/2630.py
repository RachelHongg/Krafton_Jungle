import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
cnt = 0
black = 0
white = 0

print(paper)

# paperCut 인자, (시작지점x, 시작지점y, 길이)
def paperCut(x, y, length):
    global cnt, black, white
    std = paper[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if  std != paper[i][j]:
                paperCut(i, j, length//2) # 1사분면
                paperCut(i, j + length//2, length//2) # 2사분면
                paperCut(i + length//2, j, length//2) # 3사분면
                paperCut(i + length//2, j + length//2, length//2 ) # 4사분면
                return
    if paper[i][j] == 1:
        black += 1
    else:
        white += 1

paperCut(0,0,N)
print(white)    
print(black)

# length/2 로 하면 float 타입이 되서 안됨.