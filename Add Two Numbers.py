Problem Link -> https://leetcode.com/problems/add-two-numbers/description/

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Function to reverse the Linked List

        # def reverse(head):
        #     curr,prev,ahead = head,None,None
        #     while curr:
        #         ahead = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = ahead
        #     return prev

        # # Function to calculate the number from Linked List digits

        # def findNumber(head):
        #     num = 0
        #     while head:
        #         num = num*10 + head.val
        #         head = head.next
        #     return num

        # l1 = reverse(l1)
        # l2 = reverse(l2)
        # n1 = findNumber(l1)
        # n2 = findNumber(l2)
        # number = n1+n2
        # if number == 0:
        #     return ListNode()
        
        # head,tail = None,None

        # while number:
        #     digit = number%10
        #     number = number//10
        #     temp = ListNode(digit)
        #     if head == None:
        #         head = temp
        #         tail = head
        #     else:
        #         tail.next = temp
        #         tail = tail.next
        # return head

        dummy = ListNode()
        temp = dummy
        carry = 0
        while (l1 != None or l2 != None) or carry:
            sum_ = 0
            if l1 != None:
                sum_ += l1.val
                l1 = l1.next
            if l2 != None:
                sum_ += l2.val
                l2 = l2.next
            sum_ += carry
            carry = sum_//10
            node = ListNode(sum_%10)
            temp.next = node
            temp = temp.next
        return dummy.next
