
class Solution:
    def longestPalindrome(self, s: str) -> str:
        print("hello")
        is_palindrome = self.is_palindrome(s)

    def is_palindrome(self, s):
        left_pointer = 0
        right_pointer = len(s)

        for index in range(len(s)//2):
            left_char = s[index]
            right_char = s[-index - 1]

            if (left_char != right_char): 
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    #s = "babad"
    s = "ababa"
    result = solution.longestPalindrome(s)
    assert(result == "bab")
