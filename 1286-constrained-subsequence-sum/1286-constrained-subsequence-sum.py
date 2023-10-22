class Solution:
    def constrainedSubsetSum(self, nums, k):
        # Harsav360 = Please understand the working of Algorithm
        # deque = collections.deque()
        # for i in range(len(A)):
        #     A[i] += deque[0] if deque else 0
        #     while len(deque) and A[i] > deque[-1]:
        #         deque.pop()
        #     if A[i] > 0:
        #         deque.append(A[i])
        #     if i >= k and deque and deque[0] == A[i - k]:
        #         deque.popleft()
        # return max(A)

        res = nums[0]
        max_heap = [(-nums[0],0)]
        for i in range(1,len(nums)):
            while i-max_heap[0][1] > k:
                heapq.heappop(max_heap)
            cur_max = max(nums[i],nums[i]-max_heap[0][0])
            res = max(res,cur_max)
            heapq.heappush(max_heap,(-cur_max,i))
        return res




        

        