Problem Link -> https://www.interviewbit.com/problems/matrix-median/

def findMedian(self, A):
        # def merge(flatten,second):
        #     temp = []
        #     i,j = 0,0
        #     while i < len(flatten) and j < len(second):
        #         if flatten[i] <= second[j]:
        #             temp.append(flatten[i])
        #             i += 1
        #         else:
        #             temp.append(second[j])
        #             j += 1
        #     while i < len(flatten):
        #         temp.append(flatten[i])
        #         i += 1
        #     while j < len(second):
        #         temp.append(second[j])
        #         j += 1
        #     flatten[:] = temp[:]
        # flatten = []
        # for i in range(len(A)):
        #     merge(flatten,A[i])
        # m = len(flatten)
        # if m%2 == 0:
        #     median = flatten[m//2] + flatten[m//2+1]
        #     median //= 2
        # else:
        #     median = flatten[m//2]
        # return median
        def countSmallerThanMid(row,mid):
            l,h = 0,len(row)-1
            while l <= h:
                md = (l+h)//2
                if row[md] <= mid:
                    l = md + 1
                else:
                    h = md-1
            return l
        low,high = 1,pow(10,9)
        n,m = len(A),len(A[0])
        while low <= high:
            mid = (low+high)//2
            cnt = 0
            for i in range(n):
                cnt += countSmallerThanMid(A[i],mid)
            if cnt <= (n*m)//2:
                low = mid+1
            else:
                high = mid-1
        return int(low)
