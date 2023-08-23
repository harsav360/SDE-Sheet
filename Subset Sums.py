Problem Link -> https://practice.geeksforgeeks.org/problems/subset-sums2234/1

def subsetSums(self, arr, N):
		# code here
		ans = []
		def solve(index,total):
		    if index >= N:
		        ans.append(total)
		        return
		    solve(index+1,total)
		    solve(index+1,total+arr[index])
		solve(0,0)
		return ans
