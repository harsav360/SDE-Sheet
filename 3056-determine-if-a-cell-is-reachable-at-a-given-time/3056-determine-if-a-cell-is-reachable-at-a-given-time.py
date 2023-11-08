class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # if sx == fx and sy == fy and t == 1:
        #     return False
        # eucDist = pow(fx-sx,2) + pow(fy-sy,2)
        # eucDist = int(sqrt(eucDist))
        # return eucDist <= t

        xDiff,yDiff = abs(sx-fx),abs(sy-fy)
        if xDiff == 0 and yDiff == 0 and t == 1:
            return False
        return max(xDiff,yDiff) <= t
        