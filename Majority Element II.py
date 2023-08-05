Problem Link -> https://leetcode.com/problems/majority-element-ii/

ef majorityElement(self, nums: List[int]) -> List[int]:
        # ans = set()
        # check = len(nums)//3
        # mp = dict()
        # for i in nums:
        #     if i in mp:
        #         mp[i] += 1
        #     else:
        #         mp[i] = 1
        #     if mp[i] > check:
        #         ans.add(i)
        # return list(ans)

        # Optimal Appraoch -> T:C -> O(N) and S:C -> O(1)
        # n = len(nums)
        # cnt1,cnt2 = 0,0
        # ele1,ele2 = float('inf'),float('inf')

        # for i in nums:
        #     if cnt1 == 0 and i != ele2:
        #         cnt1 = 1
        #         ele1 = i
        #     elif cnt2 == 0 and i != ele1:
        #         cnt2 = 1
        #         ele2 = i
        #     elif ele1 == i:
        #         cnt1 += 1
        #     elif ele2 == i:
        #         cnt2 += 1
        #     else:
        #         cnt1 -= 1
        #         cnt2 -= 1
        # ans = []
        # cnt1,cnt2 = 0,0
        # for i in nums:
        #     if i == ele1:
        #         cnt1 += 1
        #     if i == ele2:
        #         cnt2 += 1
        # n = int(n/3)+1
        # if cnt1 >= n:
        #     ans.append(ele1)
        # elif cnt2 >= n:
        #     ans.append(ele2)
        # return ans


        n = len(nums) # size of the array

        cnt1, cnt2 = 0, 0 # counts
        el1, el2 = float('-inf'), float('-inf') # element 1 and element 2

        # applying the Extended Boyer Moore’s Voting Algorithm:
        for i in range(n):
            if cnt1 == 0 and el2 != nums[i]:
                cnt1 = 1
                el1 = nums[i]
            elif cnt2 == 0 and el1 != nums[i]:
                cnt2 = 1
                el2 = nums[i]
            elif nums[i] == el1:
                cnt1 += 1
            elif nums[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ls = [] # list of answers

        # Manually check if the stored elements in
        # el1 and el2 are the majority elements:
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if nums[i] == el1:
                cnt1 += 1
            if nums[i] == el2:
                cnt2 += 1

        mini = int(n / 3) + 1
        if cnt1 >= mini:
            ls.append(el1)
        if cnt2 >= mini:
            ls.append(el2)

        # Uncomment the following line
        # if it is told to sort the answer array:
        #ls.sort() #TC --> O(2*log2) ~ O(1);

        return ls
