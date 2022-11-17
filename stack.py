class Stack:
    def __init__(self):
        self.stack = []
 
    def is_empty(self):
        return self.stack == []
 
    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return  self.stack[-1]
 
    def pop_it(self):
        if self.stack == []:
            return None
        else:
            return self.stack.pop()

    def size_it(self):
        return len(self.stack)
 
def balanced(s):
    stack = Stack()
    pairs = ['()', '{}', '()']
    bopen = [x[0] for x in pairs]
    bclose = [x[1] for x in pairs]
    if stack.size_it()%2 == 0:
        for c in s:
            if c in bopen:
                stack.push(c)
            elif c in bclose:
                if stack == []:
                    return 'Несбалансированно'
                else:
                    if f'{stack.peek()}{c}' in pairs:
                        stackTop = stack.pop_it()
                    else:
                        return 'Несбалансированно'
        return 'Сбалансированно'
    else:
        return "Несбалансировано"

string = '[([])((([[[]]])))]{()}'
print(balanced(string))
 
