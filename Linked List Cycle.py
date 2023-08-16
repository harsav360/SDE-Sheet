Problem Link -> https://leetcode.com/problems/linked-list-cycle/

# One Brute Force approach is to use dictionary to hash the nodes, and checking whether that particular node is already available or not
# Second approach is to use Slow and Fast pointer.

def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
