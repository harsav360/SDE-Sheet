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

        # def back(res,c):
        #     if c != '#':res.append(c)
        #     elif res:res.pop()
        #     return res
        # return reduce(back,s,[]) == reduce(back,t,[])

        # Optimized Approach

        def nextValidChar(str,index):
            backspace = 0
            while index >= 0:
                if backspace == 0 and str[index] != '#':
                    break
                elif str[index] == '#':
                    backspace += 1
                else:
                    backspace -= 1
                index -= 1
            return index

        index_s,index_t = len(s)-1,len(t)-1
        while index_s >= 0 or index_t >= 0:
            index_s,index_t = nextValidChar(s,index_s),nextValidChar(t,index_t)
            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""

            if char_s != char_t:
                return False
            index_s -= 1
            index_t -= 1
        return True
            

        


        