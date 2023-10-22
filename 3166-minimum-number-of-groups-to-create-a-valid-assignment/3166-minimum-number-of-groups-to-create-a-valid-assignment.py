class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        # mp = {}
        # for i in nums:
        #     mp[i] = 1 + mp.get(i,0)
        c = Counter(nums)
        
        if len(c) == 1:
            return 1
        
        def search(num):
            ans = 0
            for key in c:
                t = c[key] % num
                if t > c[key] // num:
                    return 0
                
                ans += ceil(c[key] / (num + 1))
                    
            return ans
        
        minn, maxx = 1, min(c.values())
        ans = float('inf')
        for i in range(minn, maxx + 1):
            s = search(i)
            if s:
                ans = min(ans, s)
                
        return ans# mini= float('inf')
        # for key in mp.keys():
        #     mini = min(mini,mp[key])
        # totalGroup = 0
        # for key in mp.keys():
        #     if mini != mp[key]:
        #         totalGroup += mp[key]-mini-1
        # totalGroup = totalGroup//2 + totalGroup%2
        # if totalGroup == 0:
        #     return len(mp)
        # else:
        #     return totalGroup + len(mp)

        
        