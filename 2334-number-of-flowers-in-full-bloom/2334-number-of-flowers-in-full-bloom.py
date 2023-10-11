class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # BFA
        # output = []
        # for person in people:
        #     ans = 0
        #     for p,q in flowers:
        #         if p <= person <= q:
        #             ans += 1
        #     output.append(ans)
        # return output

        # Binary Search Approach

        def Bs(person):
            return bisect_right(start,person)-bisect_left(end,person)

        output = []
        start = sorted(a for a,b in flowers)
        end = sorted(b for a,b in flowers)
        for person in people:
            output.append(Bs(person))
        return output



        