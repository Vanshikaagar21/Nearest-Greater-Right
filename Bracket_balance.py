querries = int(input())
i = 0
flag = 0
s = str()
stack = []
for i in range(querries):
    s = input()
    for x in s:
        if x == '(' or x == '[' or x == '{':
            stack.append(x)
        else:
            if not stack:
                flag = 1
            else:
                a = stack.pop()
                if x == ')' and a != '(' or x == '}' and a != '{' or x == ']' and a != '[':
                    flag = 1
    if flag == 1:
        print('NO')
        flag = 0
    elif x in stack:
        print('NO')
        flag = 0
    else:
        print("YES")
