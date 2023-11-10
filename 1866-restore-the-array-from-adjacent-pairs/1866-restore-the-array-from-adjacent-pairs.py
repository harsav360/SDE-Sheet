class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def solve(number,ans,visited):
            if n == len(visited):
                return ans
            ans.append(number)
            visited.add(number)
            for ngh in mp[number]:
                if ngh not in visited:
                    return solve(ngh,ans,visited)
            return ans
        ans = []
        mp = defaultdict(list)
        for u,v in adjacentPairs:
            mp[u].append(v)
            mp[v].append(u)
        first = -1
        for key in mp.keys():
            if len(mp[key]) == 1:
                first = key
                break
        visited = set()
        n = len(mp.keys())
        return solve(first,ans,visited)

            

        