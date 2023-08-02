Problem Link -> https://www.codingninjas.com/studio/problems/873366?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0


def missingAndRepeating(arr, n):

    # Write your code here
    # mp = dict()
    # for i in arr:
    #     if i in mp:
    #         repeat = i
    #     else:
    #         mp[i] = 1
    # givenSum = sum(arr)
    # resultant = givenSum-repeat
    # Nsum = (n*(n+1))//2
    # misNum = Nsum-resultant
    # return [misNum,repeat]

    Sgiven = sum(arr)
    Sn = ((n)*(n+1))//2
    SumDiff = Sgiven - Sn

    Ssquare = 0
    for i in arr:
        Ssquare += i*i
    SsquareN = (n)*(n+1)*(2*n+1)
    SsquareN //= 6
    SquareDiff = Ssquare - SsquareN
    SquareDiff //= SumDiff
    repeating = (SquareDiff+SumDiff)//2
    missing = SquareDiff - repeating
    return [missing,repeating]
