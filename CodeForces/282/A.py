t = int(input())
x = 0
for i in range(t):
    s=input()
    for i in s:
        if i == '+':
            x += 1
            break
        elif i == '-':
            x -= 1
            break

print(x)