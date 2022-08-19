from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos = 0
        
        dummy = head
        
        while dummy:
            dummy = dummy.next
            pos += 1
        
        for i in range(pos//2):
            head = head.next
        
        return head

if __name__ == "__main__":
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = solution.middleNode(node1)

    print(result)