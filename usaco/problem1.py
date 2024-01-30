def find_preferred_hay(test_cases):
    results = []
    for cows in test_cases:
        n = cows[0]
        preferences = cows[1]

        hay_count = {}
        for pref in preferences:
            hay_count[pref] = hay_count.get(pref, 0) + 1

        majority_count = n // 2 + 1
        possible_hay = []

        for hay, count in hay_count.items():
            if count >= majority_count:
                possible_hay.append(hay)

        if len(possible_hay) == 0:
            results.append([-1])
        else:
            total_count = sum(hay_count[hay] for hay in possible_hay)
            if total_count >= majority_count:
                results.append(sorted(possible_hay))
            else:
                results.append([-1])

    return results


if __name__ == "__main__":
    t = int(input())
    test_cases = []

    for _ in range(t):
        n = int(input())
        preferences = list(map(int, input().split()))
        test_cases.append((n, preferences))

    results = find_preferred_hay(test_cases)

    for result in results:
        print(*result)
