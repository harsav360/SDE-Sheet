Problem Link -> https://www.codingninjas.com/studio/problems/1062679?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    low,high = 1,m
    while low <= high:
        mid = (low+high)//2
        cal = pow(mid,n)
        if cal == m:
            return mid
        elif cal < m:
            low = mid+1
        else:
            high = mid-1
    return -1
