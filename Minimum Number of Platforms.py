Problem Link -> https://www.codingninjas.com/studio/problems/minimum-number-of-platforms_799400?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


def calculateMinPatforms(at, dt, n):
    # Write your code here.
    at.sort()
    dt.sort()
    plat,ans = 1,1
    i,j = 1,0
    while i < n and j < n:
        if at[i] <= dt[j]:
            plat += 1
            i += 1
        elif at[i] > dt[j]:
            plat -= 1
            j += 1
        if plat > ans:
            ans = plat
    return ans
