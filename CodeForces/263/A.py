matrix = [list(map(int, input().split())) for i in range(5)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1: 
            posof1 = (i,j)
            break

center = (3,3)
import math
distance = math.sqrt((3-posof1[0])**2 + (3-posof1[1])**2)

print(math.ceil(distance))