class Solution:
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
    removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric 
    characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
    """

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        backwards = ""
        forward = ""
        j = len(s)
        for i in range(len(s)):
            j -= 1
            if s[i].isalnum():
                forward += s[i] 
            if s[j].isalnum():
                backwards += s[j]

        return forward == backwards 
            

        


if __name__ == "__main__":
    solution = Solution()

    s = "A man, a plan, a canal: Panama"
    #Explanation: "amanaplanacanalpanama" is a palindrome.
    res = solution.isPalindrome(s)
    assert res == True

    s = "0P"
    res = solution.isPalindrome(s)
    assert res == False


        