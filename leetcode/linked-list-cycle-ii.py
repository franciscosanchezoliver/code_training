from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = set()
        curr = head
        while curr:
            if curr in m: return curr
            m.add(curr)
            curr = curr.next
        return None



if __name__ == "__main__":
    solution = Solution()

    node3 = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode()
    node4 = ListNode(4)

    node3.next = node2
    node2.next = node0
    node0.next = node4
    node4.next = node2

    result = solution.detectCycle(node3)

    t = [-1,-7,7,-4,19,6,-9,-5,-2,-5]
    head = ListNode(t[0])
    dummy = head
    for i in range(1, len(t)):
        head.next = ListNode(t[i])
        head = head.next
    
    result = solution.detectCycle(dummy)

    print(result)
