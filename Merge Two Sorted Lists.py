Problem Link -> https://leetcode.com/problems/merge-two-sorted-lists/

# Brute Force Approach

        # def merge(list1,list2):
        #     head,tail = None,None
        #     while list1 != None and list2 != None:
        #         if list1.val > list2.val:
        #             number = list2.val
        #             list2 = list2.next
        #         else:
        #             number = list1.val
        #             list1 = list1.next
        #         temp = ListNode(number)
        #         if head == None:
        #             head = temp
        #             tail = temp
        #         else:
        #             tail.next = temp
        #             tail = tail.next
        #     while list1:
        #         number = list1.val
        #         temp = ListNode(number)
        #         if head == None:
        #             head = temp
        #             tail = temp
        #         else:
        #             tail.next = temp
        #             tail = tail.next
        #         list1 = list1.next
        #     while list2:
        #         number = list2.val
        #         temp = ListNode(number)
        #         if head == None:
        #             head = temp
        #             tail = temp
        #         else:
        #             tail.next = temp
        #             tail = tail.next
        #         list2 = list2.next
        #     return head

        # return merge(list1,list2)

# Without Using Any extra space
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = None 
        
        
        first = list1
        second = list2
        
        if first is None:
            return list2
        if second is None:
            return list1
        
        while first and second:
            if first.val < second.val:
                if head is None:
                    head = tail = first
                else:
                    tail.next = first
                    tail = first
                first = first.next
            else:
                if head is None:
                    head = tail = second
                else:
                    tail.next = second
                    tail = tail.next
                second = second.next
        if second:
            tail.next = second
        if first:
            tail.next = first
        return head
