# Stack class
class Stack:

    def __init__(self) -> None:
        """Instantiating the Stack"""
        self.items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not self.items 

    def push(self, item):
        """Add new items to the stack"""
        self.items.append(item)

    def pop(self):
        """Pop the last Element in the Stack"""
        return self.items.pop() 

    def peek(self):
        """Check the last element in the Stack"""
        return self.items[-1]

    def size(self):
        """Check the size of the stack"""
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

if __name__ == '__main__':
    stack = Stack()
    # print(stack.is_empty())
    stack.push(20)
    stack.push(30)
    stack.push(57)
    stack.push(50)
    stack.push(51)

    print(stack)

    print(stack.peek())
    print(stack.size())
