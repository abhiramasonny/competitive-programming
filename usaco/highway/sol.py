N = int(input())
arr = []
for i in range(N):
    a,b,c = input().split()
    b,c = int(b), int(c)
    arr.append((a,b,c))
    
    


mostprecisebefore = [0,1001]
onoff = []
for i in arr:
    if i[0] == 'none':
        #print(i)
        if i[1] > mostprecisebefore[0]: 
            mostprecisebefore[0] = i[1]
        if i[2] < mostprecisebefore[1]: 
            mostprecisebefore[1] = i[2]
    else:
        onoff.append(i)

for i in onoff:
    if i[0] == 'on':
        mostprecisebefore[0] -= i[2]
        mostprecisebefore[1] -= i[1]

print("".join(mostprecisebefore))

for i in onoff:
    if i[0] == 'on':
        mostprecisebefore[0] += i[2]
        mostprecisebefore[1] += i[1]
        
    if i[0] == 'off':
        mostprecisebefore[0] -= i[2]
        mostprecisebefore[1] -= i[1]
print("".join(mostprecisebefore))