class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Brute Force Approach
        # for i in range(16):
        #     power = 4**i
        #     if power == n:
        #         return True
        #     if power > n:
        #         return False
        # return False

        # Mathematical Approach
        if n == 1:
            return True
        if n <= 0:
            return False
        
        logBase4 = math.log(n)/math.log(4)
        return logBase4 == int(logBase4)

        