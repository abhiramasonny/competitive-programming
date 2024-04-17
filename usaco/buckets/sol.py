f = open("blist.in")
n = int(f.readline())
arr = []
max_end = 0
for i in range(n):
    a,b,c = f.readline().split()
    arr.append((int(a),int(b),int(c)))
    if int(b) > max_end: max_end=int(b)
    
times = [0 for i in range(max_end+1)]

for i in arr:
    a,b,c = i
    for j in range(a,b+1):
        times[j] += c

print(max(times), file=open("blist.out", "w"))

# 0 0 0 0 