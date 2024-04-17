N = int(input())
cows = []

def flip(a, x,y):
    for i in a:
        print(i)
    print()
    print(f"{x}, {y}")
    for i in range(x+1):
        for j in range(y+1):
            if a[i][j] == 0:
                a[i][j] = 1
            else: 
                a[i][j] = 0
    for i in a:
        print(i)
    print()
    return a

for i in range(N):
    a = input()
    tmp = []
    for j in a:
        tmp.append(int(j))
    cows.append(tmp)
    
x,y = N-1,N-1
flipcounter = 0
while x>=0 and y>=0:
    if cows[x][y] == 1:
        flipcounter+=1
        cows = flip(cows,x,y)
    if x>0:
        x-=1
    else:
        y-=1
        x=y
           
        
        


print(flipcounter)