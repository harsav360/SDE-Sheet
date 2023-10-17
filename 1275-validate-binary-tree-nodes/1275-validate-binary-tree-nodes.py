# from collections import deque
# class Solution:
#     def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
#         # s = set()
#         # for i in range(n):
#         #     if leftChild[i] != -1 and leftChild[i] in s:
#         #         return False
#         #     else:
#         #         s.add(leftChild[i])
#         #     if rightChild[i] != -1 and rightChild[i] in s:
#         #         return False
#         #     else:
#         #         s.add(rightChild[i])
#         #     if leftChild[i] != -1 or rightChild[i] != -1:
#         #         s.add(i)
#         # return True

#         # root = 0
#         # childrenNodes = set(leftChild+rightChild)
#         # for i in range(n):
#         #     if i not in childrenNodes:
#         #         root = i
#         # visited = set()
#         # queue = deque([root])
#         # while queue:
#         #     node = queue.popleft()
#         #     if node in visited:
#         #         return False
#         #     visited.add(node)
#         #     if leftChild[node] != 1:
#         #         queue.append(leftChild[node])
#         #     if rightChild[node] != -1:
#         #         queue.append(rightChild[node])
#         # return len(visited) == n

from collections import deque

class Solution:
	def validateBinaryTreeNodes(self, n, leftChild, rightChild):
		# find the root node, assume root is node(0) by default
		# a node without any parent would be a root node
		# note: if there are multiple root nodes => 2+ trees
		root = 0
		childrenNodes = set(leftChild + rightChild)
		for i in range(n):
			if i not in childrenNodes:
				root = i
		
		# keep track of visited nodes
		visited = set()
		# queue to keep track of in which order do we need to process nodes
		queue = deque([root])
		
		while queue:
			node = queue.popleft()
			if node in visited:
				return False
			
			# mark visited
			visited.add(node)
			
			# process node
			if leftChild[node] != -1:
				queue.append(leftChild[node])
			if rightChild[node] != -1:
				queue.append(rightChild[node])
				
		# number of visited nodes == given number of nodes
		# if n != len(visited) => some nodes are unreachable/multiple different trees
		return len(visited) == n        
