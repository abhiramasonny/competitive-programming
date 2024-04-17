n = int(input())
cows = list(input().split())

tmp = []
for i in cows:
    tmp.append(int(i))
cows = tmp

out = []

evenmumbers = 0
oddnumbers = 0

for i in cows:
    if i%2==0:
        evenmumbers+=1
    else:
        oddnumbers+=1

while oddnumbers>evenmumbers:
    oddnumbers-=2
    evenmumbers+=1

    print(f"{evenmumbers}, {oddnumbers}")
    
if evenmumbers>oddnumbers+1:
    evenmumbers=oddnumbers+1

print(evenmumbers+oddnumbers)