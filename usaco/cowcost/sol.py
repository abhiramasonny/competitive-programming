import itertools


N,M = input().split()

cows = []
ac = []

for i in range(int(N)):
    s,t,c = input().split()
    cows.append((s,t,c))
    
for i in range(int(M)):
    a,b,p,m = input().split()
    ac.append((a,b,p,m))


print("AC: "+ str(ac))
print("cows "+ str(cows))

perm = []
for i in range(1,len(ac)+1):
    perm.extend(list(itertools.permutations(ac, r=i)))

lower = 101
upper = -1
for i in perm:
    print(i)
    
print()

for i in cows:
    if int(i[0])<lower:
        lower=int(i[0])
    elif int(i[1])>upper:
        upper=int(i[1])
        
acs_in_cows = []
for i in perm:
    tmp = [0 for j in range(upper)]
    
    for j in i:
        for k in range(len(tmp)):
            if int(k) >=int(j[0]) and int(k)<=int(j[1]):
                tmp[k]+=int(j[2])
    dosntwork= True
    for c in cows:
        print(c[0])
    
    if not(dosntwork): acs_in_cows.append(tmp)
    
for i in acs_in_cows:
    print(i)
    
            