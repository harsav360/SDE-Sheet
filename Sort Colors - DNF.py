Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Problem Link -> https://leetcode.com/problems/sort-colors/description/

ef sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # The brute force can be to use library sort Algorithm
        # T:C -> O(NlogN) and Stack Space of O(N)

        # nums.sort()

        # The optimal Solution can be DNF Algo.
        # T:C -> O(N) and S:C -> O(1)

        zero,one,two = 0,0,len(nums)-1
        while one <= two:
            if nums[one] == 0:
                nums[zero],nums[one] = nums[one],nums[zero]
                zero += 1
                one += 1
            elif nums[one] == 1:
                one += 1
            else:
                nums[two],nums[one] = nums[one],nums[two]
                two -= 1
