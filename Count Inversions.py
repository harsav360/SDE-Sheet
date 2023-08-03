Problem Link -> https://www.codingninjas.com/studio/problems/count-inversions_615?leftPanelTab=0

def getInversions(arr, n) :
	# Write your code here.
    # cnt = 0
    # for i in range(n-1):
    #     for j in range(i+1,n):
    #         if arr[i] > arr[j]:
    #             cnt  += 1
    # return cnt # T:C -> O(N^2), S:C -> O(1)

    def merge(low,mid,high):
        left = low
        right = mid+1
        temp = []
        cnt = 0

        while left <= mid and right <= high:
            if (arr[left] <= arr[right]):
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                cnt += (mid-left+1)
                right += 1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(low,high+1):
            arr[i] = temp[i-low]
        return cnt

    def mergeSort(low,high):
        cnt = 0
        if low >= high:
            return cnt

        mid = math.floor((low+high)/2)
        cnt += mergeSort(low,mid)
        cnt += mergeSort(mid+1,high)
        cnt += merge(low,mid,high)
        
        return cnt
        
    n = len(arr)
    ans = mergeSort(0,n-1)
    return ans
