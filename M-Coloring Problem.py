Problem Link -> https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#

def graphColoring(graph, k, V):
    # from collections import defaultdict
    # #your code here
    # def isSafe(node,adjList,color,k,col):
    #     for p in adjList[node]:
    #         if color[p] == col:
    #             return False
    #     return True
    
    # def solve(node,adjList,color,k,V):
    #     if node == V:
    #         return True
    #     for i in range(1,k+1):
    #         if isSafe(node,adjList,color,k,i):
    #             color[node] = i
    #             if solve(node+1,adjList,color,k,V):
    #                 return True
    #             color[node] = 0
    #     return False
                
                
    
    
    # adjList = defaultdict(list)
    # for i,j in graph:
    #     adjList[i].append(j)
    #     adjList[j].append(i)
    # color = [0]*V
        
    # return solve(0,adjList,color,k,V)
    
    
    
    assigned_colors = [-1] * V  # Initially all colors have -1 value

    def same_adj_vertex_color(ind_v, color):
        for ind_g in range(len(graph[0])):
            if graph[ind_v][ind_g] == 1 and assigned_colors[ind_g] == color:
                return True
        return False

    def dfs(ind_v=0): # BY default its value is zero if we didn't pass anything from our side
        if ind_v == V: # If it reached last Vertex, means we had successfully colored all the edges
            return True

        for color in range(k):
            if not same_adj_vertex_color(ind_v, color): # Check if it is possible to color the edge
                assigned_colors[ind_v] = color
                if dfs(ind_v + 1): # Will not proceed further if we got the True value
                    return True
                assigned_colors[ind_v] = -1 # If we didn't got the True value, then we have to change the updated color, this is the main step of backtracking
        return False # Will return false if we haven't find any True value.

    
    return dfs() # this function will return true if it is possible to color the graph else False
