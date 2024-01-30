def solve(N, S, locations):
    broken_targets = set()
    power = 1
    direction = 1
    steps = []

    while True:
        if S in broken_targets:
            break

        if locations[S][0] == 0:
            broken_targets.add(S)
        else:
            power += locations[S][1]
            direction *= -1

        steps.append(S)
        S += power * direction

        if S < 1 or S > N:
            break

    return len(broken_targets), steps

# Read input from terminal
N, S = map(int, input().split())
locations = {}
for i in range(1, N+1):
    q, v = map(int, input().split())
    locations[i] = (q, v)

# Call the solve function
result, steps = solve(N, S, locations)
print(result)

# Print the steps taken by Bessie
for step in steps:
    print(f"Bessie moves to coordinate {step}")
