def twostacks(x, a, b):
    s = c = i = j = 0
    while i < len(a) and s + a[i] <= x:
        s += a[i]
        i += 1
        c += 1
    while j < len(b) and i >= 0:
        s += b[j]
        j += 1
        while i > 0 and s > x:
            i -= 1
            s -= a[i]
        if s <= x and c < i + j:
            c = i + j
    return c


g = int(input())
for gi in range(g):
    nmx = input().split()
    n = int(nmx[0])
    m = int(nmx[1])
    x = int(nmx[2])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    print(twostacks(x, a, b))
