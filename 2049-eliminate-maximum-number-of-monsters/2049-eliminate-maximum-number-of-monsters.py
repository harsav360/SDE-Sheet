class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        timeTaken = []
        for i in range(len(dist)):
            timeTaken.append((dist[i]-1)/speed[i])
        timeTaken.sort()
        ans = 0
        for i in range(len(timeTaken)):
            if timeTaken[i] < i:
                return i
        return len(dist)

        