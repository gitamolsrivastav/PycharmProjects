def isBalP(expn):
    #expn = "{()}[]"
    stk =[]
    for ch in expn:
        if ch == '(' or ch == '{' or ch == '[':
            stk.append(ch)
        elif ch == ')':
            if stk.pop() != '(':
                return False
        elif ch == '}':
            if stk.pop() != '{':
                return False
        elif ch == ']':
            if stk.pop() != '[':
                return False
    return True

print(isBalP("{(})[]"))




