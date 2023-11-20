import sys

n = int(sys.stdin.readline())

a_list = []
length = 0

for _ in range(n):
    a = sys.stdin.readline().split() 
    
    length = len(a_list)
    if(a[0] == "push"):
        a_list.append(a[1])
    elif(a[0] == "top"):
        if(length > 0):
            print(a_list[- 1])
        else:
            print(-1)
    elif(a[0] == "size"):
        print(length)
    elif(a[0] == "empty"):
        if(length == 0):
            print(1)
        else:
            print(0)
    elif(a[0] == "pop"):
        if(length > 0):
            print(a_list[- 1])
            a_list.pop()
        else:
            print(-1)

    