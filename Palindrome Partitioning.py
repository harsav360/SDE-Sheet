Problem Link -> https://leetcode.com/problems/palindrome-partitioning/

def partition(self, s: str) -> List[List[str]]:
        ans = []
        def solve(s,path):
            if len(s) == 0:
                ans.append(path[:])
                return
            for i in range(len(s)):
                temp = s[:i+1]
                if temp == temp[::-1]:
                    solve(s[i+1:],path+[temp])
        solve(s,[])
        return ans
