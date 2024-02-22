class MyStack:
    def __init__(self):
        self.stack=[]
    def push(self, x: int) -> None:
        self.stack.append(x)
        print(self.stack)

    def pop(self) -> int:
        temp=self.stack.pop()
        return temp

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        else:
            False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()