Problem Link -> https://leetcode.com/problems/intersection-of-two-linked-lists/

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # Brute Force Approach

        # ptr1,ptr2 = headA,headB
        # while ptr1 != None:
        #     while ptr2 != None:
        #         if ptr1 == ptr2:
        #             return ptr2
        #         ptr2 = ptr2.next
        #     ptr2 = headB
        #     ptr1 = ptr1.next
        # return None

        # Hashing Approach

        # mp = {}
        # ptr1,ptr2 = headA,headB
        # while ptr1:
        #     mp[ptr1] = 1
        #     ptr1 = ptr1.next
        # while ptr2:
        #     if ptr2 in mp:
        #         return ptr2
        #     ptr2 = ptr2.next
        # return None

        # Optimal - Counting Approach

        # ptr1,ptr2 = headA,headB
        # count1,count2 = 0,0
        # while ptr1:
        #     count1 += 1
        #     ptr1 = ptr1.next
        # while ptr2:
        #     count2 += 1
        #     ptr2 = ptr2.next
        # diff = abs(count1-count2)
        # ptr1,ptr2 = headA,headB
        # if count1 > count2:
        #     while diff:
        #         ptr1 = ptr1.next
        #         diff -= 1
        # if count2 > count1:
        #     while diff:
        #         ptr2 = ptr2.next
        #         diff -= 1
        # while ptr1 != ptr2:
        #     ptr1 = ptr1.next
        #     ptr2 = ptr2.next
        # return ptr1

        ptr1,ptr2 = headA,headB
        while ptr1 != ptr2:
            ptr1 = headB if ptr1 == None else ptr1.next
            ptr2 = headA if ptr2 == None else ptr2.next
        return ptr2
