storagea = input().split()
storageb = input().split()

allpossiblea = set()

def recurse(d,numTankA,stoaragea, numTankB, stoarageb):
    if d==4:
        allpossiblea.add(numTankA)
        return

    for i in range(len(stoaragea)):
        a_val=int(stoaragea[i])
        tmpa = stoaragea.copy()
        
        del tmpa[i]
        tmpb = stoarageb.copy()
        
        tmpb.append(a_val)
            
        recurse(d+1, numTankB+a_val, tmpb, numTankA-a_val, tmpa)

recurse(0,1000,storagea,1000,storageb)
#print(allpossiblea)

total = 0
for i in allpossiblea:
    total+=1
    
print(total)