def nsr(l1):
    stack = []
    ans = []
    for i in l1[::-1]:
        if not stack:
            ans.append(len(l1))
            stack.append(i)
        else:
            if stack[-1] <= i:
                ans.append(l1.index(stack[-1]))
                stack.append(i)
            else:
                while stack and stack[-1] >= i:
                    stack.pop()
                if not stack:
                    ans.append(len(l1))
                else:
                    ans.append(l1.index(stack[-1]))
                stack.append(i)
    print(ans[::-1])
    return ans[::-1]


def nsl(l1):
    stack = []
    ans = []
    for i in l1:
        if not stack:
            ans.append(-1)
            stack.append(i)
        else:
            if stack[-1] <= i:
                ans.append(l1.index(stack[-1]))
                stack.append(i)
            else:
                while stack and stack[-1] >= i:
                    stack.pop()
                if not stack:
                    ans.append(-1)
                else:
                    ans.append(l1.index(stack[-1]))
                stack.append(i)
    return ans


def mah(l1):
    a = []
    for (i, j, k) in zip(l1, nsr(l1), nsl(l1)):
        a.append((j - k - 1) * i)
    print(max(a))

l1 = list(map(int, input().split()))
mah(l1)
