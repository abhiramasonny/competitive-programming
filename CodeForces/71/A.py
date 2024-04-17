t = int(input())
for i in range(t):
    word = input()
    if len(word) > 10:
        first = word[0]
        last = word[-1]
        list_word = list(word)
        print(f"{first}{len(word) - 2}{last}")
    else:
        print(word)