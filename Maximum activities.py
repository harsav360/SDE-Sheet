Problem Link -> https://www.codingninjas.com/studio/problems/1062712?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

def maximumActivities(start, finish):
    # Write your Code here.

    temp = []
    for i in range(len(start)):
        temp.append([start[i],finish[i]])
    temp.sort(key = lambda x:x[1])
    ans = 1
    last = temp[0][1]
    for i in range(1,len(start)):
        if last <= temp[i][0]:
            ans += 1
            last = temp[i][1]
    return ans
