class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        # if self.items:
            # return self.items[len(self.items) - 1]
        if not self.is_empty():
            return self.items[-1]

# myStack = Stack()
# myStack.push(1)
# myStack.push(2)
# myStack.push(3)
# myStack.push(4)
# print(myStack.get_stack())
# print(myStack.pop())
# print(myStack.get_stack())
# print(myStack.is_empty())
# print(myStack.peek())