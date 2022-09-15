from itertools import count
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # In the dictionary we are going to store as the key the count of 
        # characters of the words.  
        # For example the word: eat 
        #   [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
        #   [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        #
        # Therefore the key in the dictionary would be the tuple and the value would be the 
        # list of each word that fits with this counts 

        res = {}
        for word in strs:

            # The english abecedary has 26 characters so we need to initialize and empty
            # array of 26 positions
            count_characters_of_word = [0] * 26 

            # Iterate the word to count the characters
            for character in word:
                position_in_array = ord(character) - ord('a')
                count_characters_of_word[position_in_array] += 1

            # For the dictionary the key can't be a list, it must be a tuple
            count_characters_of_word = tuple(count_characters_of_word)

            # Add the word the list of words that fulfill with the count of characters
            if count_characters_of_word not in res:
                res[count_characters_of_word] = []
                res[count_characters_of_word].append(word)
            else:
                res[count_characters_of_word] .append(word)
        
        return list(res.values())
            


if __name__ =="__main__":
    solution = Solution()

    strs = ["eat","tea","tan","ate","nat","bat"]
    expected_result = [["bat"],["nat","tan"],["ate","eat","tea"]]
    result = solution.groupAnagrams(strs)

    print("expected result: " + str(expected_result))
    print("result: " + str(result))

# NOTES
# In Dictionary, the key must be unique and immutable. This means that a Python Tuple can be a
# key whereas a Python List can not. A Dictionary can be created by placing a sequence of elements 
# within curly {} braces, separated by ‘comma’.

# Sometimes, when the KeyError is raised, it might become a problem. To overcome this Python introduces 
# another dictionary like container known as Defaultdict which is present inside the collections module.

# The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict 
# never raises a KeyError. It provides a default value for the key that does not exists.


