class Solution:

    def minWindow(self, s: str, t: str) -> str:
        res = []
        res_left, res_right = None, None
        l, r = 0, 0
        have, need = 0, 0

        # Count the number of characters in each
        counter_s, counter_t = {}, {}
        for c in t:
            need += 1 # The number of conditions needed 
            counter_t[c] = 1 + counter_t.get(c, 0)

        # if character in right is in destiny
        while r < len(s) - 1 and l <= r:
            if s[r] in counter_t:
                # Add 1 to the counter
                counter_s[s[r]] = 1 + counter_s.get(s[r], 0)

                if counter_s[s[r]] <= counter_t[s[r]]:
                    have += 1

                if have == need:
                    print("Result found: " + s[l, r] + " , ({})".format(len(s[l,r])))
                    res.append(s[l, r])

                # Advance the left pointer trying to get a smaller result
                # update the map 
                if l < r:
                    counter_s[s[l]] = counter_s[s[l]] - 1 
                    if s[l] in t:
                        # If the character that abandon in the left was in the destiny
                        # then decrement the have condition
                        have -= 1
                    l += 1
                else:
                    r += 1


            while(s[r] not in counter_t):
                r += 1 

        print(res)

        print(counter_t)


if __name__ == "__main__":
    solution = Solution()

    s = "ADOBECODEBANC"
    t = "ABC"
    res = solution.minWindow(s, t)
    assert res == "BANC"
