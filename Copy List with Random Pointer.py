Problem Link -> https://leetcode.com/problems/copy-list-with-random-pointer/

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # First Approach is to use Hash Map

        # if not head:
        #     return
        # curr,mp = head,{}
        # while curr:
        #     mp[curr] = Node(curr.val,None,None)
        #     curr = curr.next
        # curr = head
        # while curr:
        #     if curr.next:
        #         mp[curr].next = mp[curr.next]
        #     if curr.random:
        #         mp[curr].random = mp[curr.random]
        #     curr = curr.next
        # return mp[head]

        # But this is using extra Space of O(N)

        # Optimal Approach -> Without using any extra space

        # First -> Make Deep Copy Connections

        curr = head
        front = head

        while curr != None:
            front = curr.next
            copy = Node(curr.val)
            curr.next = copy
            copy.next = front
            curr = front
        
        # Second -> Readjust the random pointer of Deep copy Linked List

        curr = head
        while curr != None:
            if curr.random != None:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Third -> Break the connections of deep and original Linked list

        curr = head
        psHead = Node(0)
        copy = psHead

        while curr != None:
            front = curr.next.next
            copy.next = curr.next
            curr.next = front
            copy = copy.next
            curr = curr.next
        return psHead.next
