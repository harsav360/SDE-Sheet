Problem Link -> https://leetcode.com/problems/remove-nth-node-from-end-of-list/


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # def countLength(head):
        #     ptr = head
        #     cnt = 0
        #     while ptr:
        #         cnt += 1
        #         ptr = ptr.next
        #     return cnt
        # length = countLength(head)
        # if length == n:
        #     return head.next
        # check = length-n-1
        # ptr = head
        # while check:
        #     ptr = ptr.next
        #     check -= 1
        # ptr.next = ptr.next.next
        # return head

        start = ListNode()
        start.next = head
        slow,fast = start,start
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return start.next
