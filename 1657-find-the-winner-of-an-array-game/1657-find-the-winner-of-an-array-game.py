class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        que = deque(arr)
        temp = 0
        if k >= len(arr):
            return max(arr)
        while True:
            first = que.popleft()
            while True:
                second = que.popleft()
                if first > second:
                    temp += 1
                    que.append(second)
                if temp == k:
                    return first
                elif first < second:
                    que.appendleft(second)
                    que.append(first)
                    temp = 1
                    break
            

        