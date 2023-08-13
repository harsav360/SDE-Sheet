Problem Link -> https://leetcode.com/problems/reverse-linked-list/

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,ahead,prev = head,None,None
        while curr:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead
        return prev
