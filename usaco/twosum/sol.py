"""4 8
2 7 5 1
"""
    
n = 4
x = 8

arr = [2,7,5,1]
"""
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i] + arr[j] == x:
            print(f"{i} {j}")
"""


dictionary = {}

for i in range(len(arr)):
    compliment = x-arr[i]
    if compliment in dictionary:
        print(f"{dictionary[compliment]} {i}")
    else:
        dictionary[arr[i]] = i


