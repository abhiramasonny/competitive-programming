N = int(input())
import itertools
milking = []

for i in range(N):
    phrase = input().split()
    firstcow = phrase[0]
    secondcow = phrase[-1]
    milking.append((firstcow,secondcow))


startinglist = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]

startinglist.sort()

allpossible = list(itertools.permutations(startinglist,8))

working = []

for i in allpossible:
    for j in milking:
        cow1,cow2 = j
        cow1_index = i.index(cow1)
        cow2_index = i.index(cow2)
        
        if abs(cow1_index-cow2_index) != 1:
            break
    else:
        a = i
        for k in a:
            print(k)
        break
