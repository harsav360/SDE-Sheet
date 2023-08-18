Problem Link -> https://leetcode.com/problems/3sum/

def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute Force Approach

        # ans = set()
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 attach = [nums[i],nums[j],nums[k]]
        #                 attach.sort()
        #                 ans.add(tuple(attach))
        # return list(ans)

        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = i+1
            l = n-1

            while k < l:
                total = nums[i] + nums[k] + nums[l]
                if total == 0:
                    ans.append([nums[i],nums[k],nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while l > k and nums[l] == nums[l+1]:
                        l -= 1
                elif total < 0:
                    k += 1
                else:
                    l -= 1
        return ans
