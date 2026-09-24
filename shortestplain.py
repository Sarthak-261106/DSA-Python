class Solution(object):
    def shortestPalindrome(self, s):

        rev = s[::-1]

        combined = s + "#" + rev

        lps = [0] * len(combined)

        i = 1
        temp = 0

        while i < len(combined):

            if combined[i] == combined[temp]:
                temp += 1
                lps[i] = temp
                i += 1

            else:
                if temp != 0:
                    temp = lps[temp - 1]
                else:
                    lps[i] = 0
                    i += 1

        longest = lps[-1]

        remaining = s[longest:]

        return remaining[::-1] + s