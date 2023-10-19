class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # stack1 = []
        # stack2 = []
        # for i in s:
        #     if i == '#' and stack1:
        #         stack1.pop()
        #     else:
        #         stack1.append(i)
        # for j in t:
        #     if j == '#' and stack2:
        #         stack2.pop()
        #     else:
        #         stack2.append(j)
        # while stack1 and stack2:
        #     if stack1.pop() != stack2.pop():
        #         return False
        # if stack1 or stack2:
        #     return False
        # return True

        def back(res,c):
            if c != '#':res.append(c)
            elif res:res.pop()
            return res
        return reduce(back,s,[]) == reduce(back,t,[])
            

        


        