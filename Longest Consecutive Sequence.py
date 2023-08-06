Problem Link -> https://leetcode.com/problems/longest-consecutive-sequence/

# Brute Force Approach -> Sorting the given array, T:C -> O(N*logN), The Sorting algo needs little bit modification, can you find?

        # nums.sort()
        # ans = 1
        # cnt = 1
        # for i in range(len(nums)-1):
        #     if nums[i]+1 == nums[i+1]:
        #         cnt += 1
        #     else:
        #         ans = max(ans,cnt)
        #         cnt = 1
        # ans = max(ans,cnt)
        # return ans
        if len(nums) <= 0:
            return 0
        st = set(nums)
        longest = 1
        cnt = 1
        n = len(nums)
        for it in st:
        # if 'it' is a starting number
            if it - 1 not in st:
            # find consecutive numbers
                cnt = 1
                x = it
                while x + 1 in st:
                    x += 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest
