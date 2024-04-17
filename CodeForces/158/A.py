n,k = map(int, input().split())
patricipents = [int(x) for x in input().split()]
k_score = patricipents[k-1]
count = 0
for i in patricipents:
    if i >= k_score and i > 0:
        count += 1
print(count)