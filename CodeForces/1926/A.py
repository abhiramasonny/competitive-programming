t = int(input())

for _ in range(t):
    s = input()
    ca = s.count('A')
    cb = s.count('B')
    
    if ca > cb:
        print('A')
    else:
        print('B')