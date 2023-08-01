Problem Link = https://leetcode.com/problems/merge-intervals/

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans = [intervals[0]]
        for i,j in intervals[1:]:
            if ans[-1][1] >= i:
                ans[-1][1] = max(ans[-1][1],j)
            else:
                ans.append([i,j])
        return ans
