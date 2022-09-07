class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Create 2 list with the inputs
        bulls, cows = 0, 0

        secret = list(secret)
        guess = list(guess)

        secret_char_counter = {}
        guess_char_counter = {}

        # Eliminate bulls from both lists. And count how many bulls
        index = 0
        while index < len(secret):
            if secret[index] == guess[index]:
                secret.pop(index)
                guess.pop(index)
                bulls += 1

            else:
                # Count the characters in the secret and the guess strings
                secret_char_counter[secret[index]] = 1 + \
                    secret_char_counter.get(secret[index], 0)
                guess_char_counter[guess[index]] = 1 + \
                    guess_char_counter.get(guess[index], 0)
                index += 1

        # Count how many cows.
        # Compare the 2 dictionaries to count the cows
        for each_key in secret_char_counter:
            value_in_secret = secret_char_counter[each_key]
            if each_key in guess_char_counter:
                value_in_guess = guess_char_counter[each_key]
                coincidences = min(value_in_secret, value_in_guess)
                cows += coincidences

        return "{}A{}B".format(bulls, cows)


if __name__ == "__main__":
    solution = Solution()
    secret = "1807"
    guess = "7810"
    res = solution.getHint(secret, guess)
    assert res == "1A3B"
