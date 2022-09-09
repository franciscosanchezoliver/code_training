class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        # Iterate over every char in the string
        for each_char in s:

            if each_char != ']':
                stack.append(each_char)

            # If the char is ']' then we have found the end of a sub problem
            else:
                # Keep track of the result of the subproblem
                subproblem_result = ""
                # We keep popping elements until a '[' is found
                while stack[-1] != '[': # It is guaranteed to find an open bracket '['
                    subproblem_result = stack.pop() + subproblem_result
                
                # After the extracting of all the characters of the subproblem we need
                # to pop another char '['. We can discard this character
                stack.pop()

                # Now we have to read how many times (k) this subproblem will be happening
                # But the number may be formed by several digits. Ex: 3242[
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k 
                
                # Once we have the subproblem resolved and K, we calculate the result and 
                # insert the result and the end of the stack
                stack.append(int(k) * subproblem_result)
            
        return "".join(stack)








if __name__ == "__main__":
    solution = Solution()
    s = "3[a]2[bc]"
    res = solution.decodeString(s)
    print(res)
    assert res == "aaabcbc"