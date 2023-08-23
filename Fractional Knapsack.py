Problem Statement -> https://www.codingninjas.com/studio/problems/fractional-knapsack_975286?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

def maximumValue(items, n, w):

	# Write your code here.
	# ITEMS contains [weight, value] pairs.
	items.sort(key = lambda x:x[1]/x[0],reverse = True)
	ans = 0
	for i in items:
		if w >= i[0]:
			ans += i[1]
			w -= i[0]
		else:
			ans += (i[1]/i[0])*w
			w = 0
		if w == 0:
			break
	return ans
