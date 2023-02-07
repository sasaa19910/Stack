class Stack:
    def __init__(self):
        self.my_stack = []


    def is_empty(self):
        if self.my_stack:
            return True
        else:
            return False


    def push(self,element):
        self.my_stack.append(element)


    def pop(self):
        result = self.my_stack.pop()
        return result

    def peek(self):
        return self.my_stack[-1]

    def size(self):
        return len(self.my_stack)





