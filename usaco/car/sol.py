n,m = map(int, input().split())

N_speeds = []
M_speeds = []
for i in range(n):
    a,b = input().split()
    N_speeds.append((int(a),int(b)))
    
for i in range(m):
    a,b = input().split()
    M_speeds.append((int(a),int(b)))
    
    
#print(N_speeds)
#print(M_speeds)

multiplied_M_speeds = []
multiplied_N_speeds = []

for i in N_speeds:
    for j in range(i[0]):
        multiplied_N_speeds.append(i[1])
        

for i in M_speeds:
    for j in range(i[0]):
        multiplied_M_speeds.append(i[1])
        
biggest_diff = 0
for i in range(100):
    if multiplied_N_speeds[i] < multiplied_M_speeds[i]:
        tmp = multiplied_M_speeds[i]-multiplied_N_speeds[i]
        if tmp>biggest_diff:
            biggest_diff = tmp
print(biggest_diff)