Problem Link -> https://leetcode.com/problems/reverse-nodes-in-k-group/


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # First, We will count the number of nodes in Linked List
        def countNode(head):
            ptr = head
            count = 0
            while ptr:
                count += 1
                ptr = ptr.next
            return count

        # Write an recursive function that will reverse the first k nodes, and then make a call for remaining
        def reverseKNode(head,limit):
            if head == None or limit < k: # Will stop if head is None or number of nodes are left than k
                return head
            prev,ahead = None,None
            curr = head
            count = 0
            while curr and count < k: # Will reverse until current is None or the count value is less than k
                ahead = curr.next
                curr.next = prev
                prev = curr
                curr = ahead
                count += 1
            limit -= k
            if ahead != None:
                head.next = reverseKNode(ahead,limit) 
            return prev
        limit = countNode(head)
        return reverseKNode(head,limit)
