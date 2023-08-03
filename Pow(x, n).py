Problem Link -> https://leetcode.com/problems/powx-n/

def myPow(self, x: float, n: int) -> float:

        # Brute Force Approach, it to multiply x upto n times

        # ans = 1
        
        # if n > 0:
        #     while n > 0:
        #         ans *= x
        #         n -= 1
        #     return ans
        # elif n < 0:
        #     while n < 0:
        #         ans /= x
        #         n += 1
        #     return ans
        # else:
        #     return 1

        # Second Approach can be to use, in-built python function

        #return pow(x,n)

        # Optimal Approach is to use concept of multiplication and power's

        nn = n
        ans = 1
        if nn < 0:
            nn *= -1
        while nn > 0:
            if nn%2 == 1:
                ans *= x
                nn -= 1
            else:
                x = x*x
                nn //= 2
        if n < 0:
            ans = 1/ans
        return ans
