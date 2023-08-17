Problem Link -> https://leetcode.com/problems/linked-list-cycle-ii/description/

def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First Appraoch -> Use hash Map

        # mp = {}
        # ptr = head
        # while ptr:
        #     if ptr in mp:
        #         return mp[ptr]
        #     mp[ptr] = ptr
        #     ptr = ptr.next
        # return None
        
        # Optimal Approach -> Use Slow and Fast Pointer Appraoch

        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == None or fast.next == None:
            return None
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast
