from typing import List, Optional

class ListNode:

    def __init__(
        self, 
        val=0,
        next=None
    ):
        self.val = val
        self.next = next

class Solution:

    def reverseList(
        self, 
        head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp_next_node = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next_node
        
        return prev



if __name__ == "__main__":

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    result = solution.reverseList(node1)
    print("end")


    