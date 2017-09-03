class Stack(object):

    def __init__(self):

        self.items = []


    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# def palStack(string):
#
#     stk = Stack()
#     l = len(string)
#     mid = l//2
#     for i in range(mid):
#         stk.push(string[i])
#     for j in range(mid+1, l):
#         if stk.pop() != string[j]:
#             return False
#     return True
#
# print(palStack("radar"))


def balancedParenthesis(expr):
    stk = Stack()
    return_array = ['YES', 'NO']
    if len(expr)%2 != 0:
        return return_array[1]
    opening = ['[', '{', '(']
    matches = [('(', ')'), ('{', '}'), ('[', ']')]

    for c in expr:
        if c in opening:
            stk.push(c)
        else:

            if stk.size() == 0:
                return False
            last_open  = stk.pop()
            if (last_open,c) not in matches:
                return False
    return return_array[0]

print(balancedParenthesis('{())}()[]'))


return_array = ['YES', 'NO']
print((return_array[0]))











