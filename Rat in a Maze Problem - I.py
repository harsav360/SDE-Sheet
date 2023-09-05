Problem Link -> https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

# class Solution:
#     def findPath(self, m, n):
#         # code here
        
#         def solve(r,c,ans,path):
#             if r == row-1 and c == col-1:
#                 ans.append(path)
#                 return
            
#             # Downward Direction
#             if r+1 < row and m[r+1][c]:
#                 m[r+1][c] = 0
#                 solve(r+1,c,ans,path+'D')
#                 m[r+1][c] = 1
            
#             # Leftward Direction
            
            
#             if c-1 >= 0 and m[r][c-1]:
#                 m[r][c-1] = 0
#                 solve(r,c-1,ans,path+'L')
#                 m[r][c-1] = 1
                
#             # Rightward Direction
            
#             if c+1 < col and m[r][c+1]:
#                 m[r][c+1] = 0
#                 solve(r,c+1,ans,path+'R')
#                 m[r][c+1] = 1
                
#             # Upward Direction
#             if r-1 >= 0 and m[r-1][c]:
#                 m[r-1][c] = 0
#                 solve(r-1,c,ans,path+'U')
#                 m[r-1][c] = 1
                
#         ans = []
#         row,col = n,n
#         solve(0,0,ans,'')
#         return ans

#User function Template for python3

class Solution:
    def findPathHelper(self, i, j, a, n, ans, move, vis):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return


        # downward
        if i + 1 < n and not vis[i + 1][j] and a[i + 1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i + 1, j, a, n, ans, move + 'D', vis)
            vis[i][j] = 0


        # left
        if j - 1 >= 0 and not vis[i][j - 1] and a[i][j - 1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i, j - 1, a, n, ans, move + 'L', vis)
            vis[i][j] = 0


        # right
        if j + 1 < n and not vis[i][j + 1] and a[i][j + 1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i, j + 1, a, n, ans, move + 'R', vis)
            vis[i][j] = 0


        # upward
        if i - 1 >= 0 and not vis[i - 1][j] and a[i - 1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i - 1, j, a, n, ans, move + 'U', vis)
            vis[i][j] = 0


    def findPath(self, m, n):
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]


        if m[0][0] == 1:
            self.findPathHelper(0, 0, m, n, ans, "", vis)
        return ans
        # code here
        # def func(i,j,y,a,b):

        #     if i==n and j==n-1:

        #         out.append(y)

        #         return

        #     if 0<=i<n and 0<=j<n and m[i][j]==1:

        #         if a+1==i:y+="D"

        #         if a-1==i:y+="U"

        #         if b+1==j:y+="R"

        #         if b-1==j:y+="L"

        #         a,b=i,j

        #         temp=m[i][j]

        #         m[i][j]=None

        #         if func(i+1,j,y,a,b) or func(i-1,j,y,a,b) or func(i,j+1,y,a,b) or func(i,j-1,y,a,b):return

        #         m[i][j]=temp

        # out=[]

        # func(0,0,"",0,0)

        # return out
