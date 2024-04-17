def count_groups(numbers):
    groups = []
    for num in numbers:
        assigned = False
        for group in groups:
            valid = True
            for n in group:
                if num & n == num:
                    valid = False
                    break
            if valid:
                group.append(num)
                assigned = True
                break
        if not assigned:
            groups.append([num])
    return len(groups)

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of integers
    n = int(input())
    # Read the integers
    numbers = list(map(int, input().split()))
    # Count the minimum number of groups
    result = count_groups(numbers)
    # Print the result
    print(result)