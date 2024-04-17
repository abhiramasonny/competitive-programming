t = int(input())
"""
Sasha decided to give his girlfriend an array 𝑎1,𝑎2,…,𝑎𝑛. He found out that his girlfriend evaluates the beauty of the array as the sum of the values (𝑎𝑖−𝑎𝑖−1) for all integers 𝑖 from 2 to 𝑛

.

Help Sasha and tell him the maximum beauty of the array 𝑎
that he can obtain, if he can rearrange its elements in any way.
"""

for i in range(t):
    a = map(list, input().split())
    a = list(map(int, input().split()))
    a.sort()
    max_beauty = sum(a[i] - a[i-1] for i in range(1, len(a)))
    print(max_beauty)