def has_equal_divisors(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and len(set(arr[i:j+1])) == 1:
                return True
    return False


def find_mode(arr):
    frequency = {}
    max_frequency = 0
    modes = []
    
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

        if frequency[num] > max_frequency:
            max_frequency = frequency[num]
            modes = [num]
        elif frequency[num] == max_frequency and num not in modes:
            modes.append(num)
    if not has_equal_divisors(arr) and not len(modes) ==1:
            return [-1]
    return modes

t = int(input())
final = []
for i in range(t):
    N = int(input())
    preferences = list(map(int, input().split()))
    ans = find_mode(preferences)
    #print("hi")
    print(*ans)