Problem Link -> https://leetcode.com/problems/rotate-list/description/

def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head == None or k == 0:
            return head
        count = 0
        ptr = head
        while ptr:
            count += 1
            ptr = ptr.next
        k = k%count
        check = count-k
        ptr1 = head
        temp = head
        while check:
            temp = ptr1
            ptr1 = ptr1.next
            check -= 1
        temp.next = None
        if ptr1 == None:
            return head
        ptr2 = ptr1
        while ptr2.next != None:
            ptr2 = ptr2.next
        ptr2.next = head
        head = ptr1 
        return head
