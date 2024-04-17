def sum_of_digits(n, memo):
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = sum(int(digit) for digit in str(n))
        return memo[n]

def calculate_total_sum(n, memo):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += sum_of_digits(i, memo)
    return total_sum

memo = [0] * 1000001

t = int(input())

for _ in range(t):
    n = int(input())
    print(calculate_total_sum(n, memo))
