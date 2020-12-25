l1 = list(map(int, input().split()))
stack = []
ans = []
count = -1
for i in l1:
    count += 1
    if not stack:
        ans.append(count - (-1))
        stack.append(i)
    else:
        if stack[-1] >= i:
            ans.append(count - l1.index(stack[-1]))
            stack.append(i)
        else:
            while stack and stack[-1] <= i:
                stack.pop()
            if not stack:
                ans.append(count - (-1))
            else:
                ans.append(count - l1.index(stack[-1]))
            stack.append(i)

print(ans)
