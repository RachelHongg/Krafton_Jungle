import sys 

N = int(input())
tree = {}

for n in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]
    
def pre_order(root):
    if root != '.':
        print(root, end='') # root
        pre_order(tree[root][0]) # left
        pre_order(tree[root][1])    # right
        
def in_order(root):
    if root != '.':
        in_order(tree[root][0]) # left
        print(root, end='') # root
        in_order(tree[root][1]) # right

def post_order(root):
    if root != '.':
        post_order(tree[root][0]) # left
        post_order(tree[root][1]) # right
        print(root, end='') # root
        
                
pre_order('A')
print()
in_order('A')       
print() 
post_order('A')