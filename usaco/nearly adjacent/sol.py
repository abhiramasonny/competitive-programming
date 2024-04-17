N = int(input())
connections = []
for i in range(N-1):
    connections.append(tuple(input().split()))
    
#print(connections)

#nearly adjacent
nearlyadjacent = []
for i in connections:
    val = int(i[1])
    for j in connections:
        if int(j[0]) == val:
            nearlyadjacent.append((str(val),j[1]))
            
total = set() #remove the duplicates

for i in connections:
    total.add(i)

for i in nearlyadjacent:
    total.add(i)
    
print(len(total))