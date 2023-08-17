Problem Link -> https://leetcode.com/problems/palindrome-linked-list/description/

def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # First Approach -> Insert the elements in an list and then compare the list from front and back
        # T:C -> O(N+N/2), S:C -> O(N), using list

        # lst = []
        # ptr = head
        # while ptr:
        #     lst.append(ptr.val)
        #     ptr = ptr.next
        # front,back = 0,len(lst)-1
        # while front <= back:
        #     if lst[front] != lst[back]:
        #         return False
        #     front += 1
        #     back -= 1
        # return True

        # Second Approach -> Create another linked list in reverse order
        # T:C = O(N+N), S:C = O(N)

        # newHead,newTail = None,None
        # ptr = head
        # while ptr:
        #     temp = ListNode(ptr.val)
        #     if newHead == None:
        #         newHead = temp
        #         newTail = temp
        #         newHead.next = None
        #     else:
        #         newTail = temp
        #         newTail.next = newHead
        #         newHead = newTail
        #     ptr = ptr.next
        # while newHead != None and head != None:
        #     if newHead.val != head.val:
        #         return False
        #     newHead = newHead.next
        #     head = head.next
        # return True

        # Third Approach -> Reverse half of the Linked List
        if head.next == None:
            return True

        slow,fast,temp = head,head,None
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None
        prev,ahead,curr = None,None,slow
        while curr:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead
        while prev != None and head != None:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
