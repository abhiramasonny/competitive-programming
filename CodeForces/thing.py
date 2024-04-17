t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 1:
        print(*range(1, n + 1))
    elif k == 2:
        print(*([10 ** 9] * (n - 2)), 1, 10 ** 9)
    else:
        print(-1)
