class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val):
        self.stack.append(val)
        val=min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        

    def pop(self):
        self.stack.pop()
        self.minstack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()