from typing import Optional

class ListNode:

    def __init__(
        self, 
        val = 0, 
        next = None
    ):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)

class Solution:

    def mergeTwoLists(
        self, 
        l1: Optional[ListNode], 
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        

        return dummy.next




if __name__ == "__main__":
    solution = Solution()

    node1_red  = ListNode(1)
    node2_red  = ListNode(2)
    node4_red  = ListNode(4)

    node1_red.next = node2_red
    node2_red.next = node4_red

    node1_blue  = ListNode(1)
    node3_blue  = ListNode(3)
    node4_blue  = ListNode(4)

    node1_blue.next = node3_blue
    node3_blue.next = node4_blue

    solution.mergeTwoLists(node1_red, node1_blue)

