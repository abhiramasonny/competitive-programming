t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    # Find the largest odd number less than or equal to n
    largest_odd = n - (n % 2 == 0)
    
    # Find the largest power of 2 less than or equal to largest_odd
    largest_power_of_2 = 2 ** (largest_odd.bit_length() - 1)
    
    # Calculate the position of the largest_power_of_2
    position = largest_power_of_2 // 2
    
    # Calculate the position of the k-th card
    while k > position:
        k -= position
        position //= 2
    
    # Calculate the value of the k-th card
    card_value = 2 * k - 1
    
    print(card_value)