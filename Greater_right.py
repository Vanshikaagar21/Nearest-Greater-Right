x1 = list(map(int, input().split()))
l1 = x1[::-1]
stack = []
ans = []
for i in l1:
    if not stack:
        ans.append(-1)
        stack.append(i)
    else:
        if stack[-1] >= i:
            ans.append(stack[-1])
            stack.append(i)
        else:
            while stack and stack[-1] <= i:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(i)
print(ans[::-1])
