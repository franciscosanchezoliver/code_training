class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        def fillStack(stack, s):
            for each_char in s:
                if each_char == "#":
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(each_char)
            return stack
        
        stack_s = fillStack(stack_s, s)
        stack_t = fillStack(stack_t, t)
        
        return stack_s == stack_t


if __name__ == "__main__":
    solution = Solution()
    #s = "ab##"
    #t = "c#d#"
    #res = solution.backspaceCompare(s, t)
    #assert res == True

    s = "y#fo##f"
    t = "y#f#o##f"
    res = solution.backspaceCompare(s, t)
    assert res == True
