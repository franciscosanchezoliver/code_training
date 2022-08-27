# https://leetcode.com/problems/longest-palindromic-substring/

from turtle import left, right


class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_palindrome = ""
        size_longest_palindrome = 0

        for i in range(len(s)):

            # odd case
            left_char, right_char = i, i
            while left_char >= 0 and right_char < len(s) and s[left_char] == s[right_char]:
                size_of_new_palindrome = right_char - left_char + 1
                if size_of_new_palindrome > size_longest_palindrome:
                    size_longest_palindrome = size_of_new_palindrome 
                    longest_palindrome = s[left_char:right_char + 1]
                left_char -= 1
                right_char += 1

            # even case
            left_char, right_char = i, i + 1
            while left_char >= 0 and right_char < len(s) and s[left_char] == s[right_char]:
                size_of_new_palindrome = right_char - left_char + 1
                if size_of_new_palindrome >= size_longest_palindrome:
                    size_longest_palindrome = size_of_new_palindrome 
                    longest_palindrome = s[left_char:right_char + 1]
                left_char -= 1
                right_char += 1

        return longest_palindrome


if __name__ == "__main__":
    solution = Solution()

    s = "babad"
    result = solution.longestPalindrome(s)
    assert result == "bab"

   # s = "cbbd"
   # result = solution.longestPalindrome(s)
   # assert result == "bb"

    s = "ccd"
    result = solution.longestPalindrome(s)
    assert result == "cc"