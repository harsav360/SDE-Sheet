class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 0


        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.mini = val
            self.stack.append(val)
        elif val < self.mini:
            temp = self.mini
            self.mini = val
            val = 2*val-temp
            self.stack.append(val)
        else:
            self.stack.append(val)

    
        

    def pop(self) -> None:
        ans = self.stack.pop()
        if ans < self.mini:
            self.mini = 2*self.mini-ans
        if len(self.stack) == 0:
            self.mini = 0
        
        

    def top(self) -> int:
        if self.stack[-1] < self.mini:
            return self.mini
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()