Problem Link -> https://leetcode.com/problems/majority-element/description/

def majorityElement(self, nums: List[int]) -> int:

        # Brute Force is to traverse on every element and check : T:C -> O(N^2) and S:C -> O(1)

        #  Better approach is to use hash map, T:C -> O(N) and S:C -> O(N)
        # mp = dict()
        # n = len(nums)
        # for i in nums:
        #     if i in mp:
        #         mp[i] += 1
        #         if mp[i] > n//2:
        #             return i
        #     else:
        #         mp[i] = 1

        # Optimal Approach -> Moore's Voting Algorithm

        cnt = 0
        ele = nums[0]

        for i in nums:
            if ele == i:
                cnt += 1
            elif cnt == 0:
                cnt = 1
                ele = i
            else:
                cnt -= 1
        return ele
