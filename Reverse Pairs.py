Problem Link -> https://leetcode.com/problems/reverse-pairs/

def reversePairs(self, nums: List[int]) -> int:

        # Brute Force -> O(N^2)

        # ans = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] > 2 * nums[j]:
        #             ans += 1
        # return ans

        def merge(arr,low,mid,high):
            temp = []
            left = low
            right = mid+1

            while left <= mid and right <= high:
                if arr[left] < arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1

            for i in range(low,high+1):
                arr[i] = temp[i-low]

        def countPair(arr,low,mid,high):
            right = mid+1
            cnt = 0
            for i in range(low,mid+1):
                while right <= high and arr[i] > 2*arr[right]:
                    right += 1
                cnt += (right-(mid+1))
            return cnt

        def mergeSort(arr,low,high):
            cnt = 0
            if low >= high:
                return cnt
            mid = (low+high)//2
            cnt += mergeSort(arr,low,mid)
            cnt += mergeSort(arr,mid+1,high)
            cnt += countPair(arr,low,mid,high)
            merge(arr,low,mid,high)
            return cnt

        return mergeSort(nums,0,len(nums)-1)
