Problem Link ->https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

def maximumMeetings(self,n,start,end):
        # code here
        check = []
        for i in range(n):
            check.append([start[i],end[i]])
        check.sort(key = lambda i:i[1])
        ans = 1
        last = check[0][1]
        for start,end in check[1:]:
            if start > last:
                ans += 1
                last = end
        return ans
