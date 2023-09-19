class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      nums = [-x for x in nums]
      heapq.heapify(nums)
      while k:
        if k == 1:
          ans = heapq.heappop(nums)
          k -= 1
        else:
          heapq.heappop(nums)
          k -= 1
      ans = -1*ans
      return ans
        