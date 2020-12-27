n = int(input())
s = ''
undo = ['']

for i in range(0, n):
    choice = list(input().split())
    k = int(choice[0])
    if k == 1:
        s += choice[1]
        undo.append(s)
    elif k == 2:
        s = s[:(-int(choice[1]))]
        undo.append(s)
    elif k == 3:
        print(s[int(choice[1]) - 1])
    elif k == 4:
        undo.pop()
        s = undo[-1]
