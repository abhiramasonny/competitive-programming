def count(N, S, locations):
    power = 1
    direction = 1
    targets_broken = 0

    while 1 <= S <= N:
        q, v = locations[S - 1]

        if q == 1 and power >= v:
            targets_broken += 1

        if q == 0:
            power += v
            direction *= -1

        S += direction * power

    return targets_broken


N, S = map(int, input().split())
locations = [list(map(int, input().split())) for _ in range(N)]

result = count(N, S, locations)
print(result)
