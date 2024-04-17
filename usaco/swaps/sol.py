N = int(input())

cows = []
for i in range(N):
    cows.append(int(input()))
    
cows = list(dict.fromkeys(cows))

#index of not sorted
print()
for i in range(len(cows)-1):
    for j in range(i+1,len(cows)):
        if cows[i]> cows[j]:
            index=j
            break
        
insert_index = 0
for i in range(len(cows)):
    if cows[i]>cows[index]:
        insert_index = i-2
        
print(index-insert_index)

