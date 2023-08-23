Problem Link -> https://www.codingninjas.com/studio/problems/find-minimum-number-of-coins_975277?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

def MinimumCoins(n: int) -> List[int]:
    # write your code here
    coins = [1000,500,100,50,20,10,5,2,1]
    i = 0
    ans = []
    while n:
        if n >= coins[i]:
            temp = n//coins[i]
            n -= coins[i]*temp
            ans.extend([coins[i]]*temp)
        i += 1
    return ans
# len_ = len(coins)
# for i in range(len_):
#         while n >= coins[i]:
#             n -= coins[i]
#             ans.append(coins[i])
