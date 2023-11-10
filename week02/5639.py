import sys
sys = input()
array = []

# 입력을 받는다.
while True:
    try:
        array.append(int(input().rstrip()))
    except:
        break

# 이진 트리 방식으로 배열에 넣는다.
def BinaryTree(root_idx, end_idx):
    # 종료 조건
    if root_idx > end_idx:
        return
    # 처음 받은 배열 저장
    global array
    
    # 만약 root보다 큰 값 없는 경우 전부 왼쪽 서브트리로 취급
    right_start = end_idx + 1
    
    for i in range(root_idx + 1, end_idx + 1):
        if array[root_idx] < array[i]:
            right_start = i
            break
    
    # root 다음부터 왼쪽 서브트리 검색
    BinaryTree(root_idx + 1, right_start - 1)

    # 왼쪽 서브트리 탐색 끝나면 오른쪽 서브트리 탐색
    BinaryTree(right_start, end_idx)

    # 왼쪽, 오른쪽 서브트리 탐색 끝나면 root출력
    print(array[root_idx])
    
BinaryTree(0, len(array) - 1)

            
    
    
    
    
    
    
        
        
            
            
    
            
             
        

# 후위 순회로 출력한다.
