n = int(input())
ans = 0
for i in range(n):
    a,b,c = map(int, input().split())
    if a == 1 and b==1:
        ans +=1
    elif a == 1 and c==1:
        ans+=1
    elif b == 1 and c==1:
        ans+=1
print(ans)