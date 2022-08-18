from typing import Optional

class ListNode:
    def __init__(
        self, 
        val=0,
        next=None
    ):
        self.val= val 
        self.next = next


class Solution:
    def addTwhoNumbers(
        self, 
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        carry = 0
        head = new_node = ListNode(0)
        while l1 or l2 or carry == 1:

            if l1 is None:
                l1 = ListNode(0)

            if l2 is None:
                l2 = ListNode(0)

            sum_of_2_digits = l1.val + l2.val + carry
            # check if has carry
            result_digit = sum_of_2_digits % 10
            if sum_of_2_digits >= 10:
                carry = 1
            else:
                carry = 0

            # Create a new node with the value
            new_node.next = ListNode(val=result_digit)
            new_node = new_node.next

            # iterate over the input lists
            l1 = l1.next
            l2 = l2.next


        return head.next




if __name__ == "__main__":
    print("hola")
    l1 = [9,2,9,9,9,9,9]
    l2 = [9,9,9,9]

    a_primer_digito = ListNode(9)
    a_segundo_digito = ListNode(9)

    a_primer_digito.next = a_segundo_digito


    b_primer_digito = ListNode(9)
    b_segundo_digito = ListNode(9)

    b_primer_digito.next = b_segundo_digito

    solution = Solution()
    solution.addTwhoNumbers(a_primer_digito, b_primer_digito)