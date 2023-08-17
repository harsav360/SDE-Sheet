Problem Link -> https://www.codingninjas.com/studio/problems/1112655?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

# Brute Force Approach -> insert all the linked list element inside an list, sort the list and then create the new linked list from the list elemets using child or bottom pointer
# But this approach will use the extra space


# Merge Sort Appraoch

def flattenLinkedList(head: Node) -> Node:
    
    def mergeTwoList(a,b):
        temp = Node(0)
        res = temp

        while a != None and b != None:
            if a.data < b.data:
                temp.child = a
                temp = temp.child
                a = a.child
            else:
                temp.child = b
                temp = temp.child
                b = b.child
        if a != None:
            temp.child = a
        else:
            temp.child = b
        return res.child

    def flatten(root):
        if root == None or root.next == None:
            return root
        root.next = flatten(root.next)
        root = mergeTwoList(root,root.next)
        return root
    
    return flatten(head)
